from PySide2.QtWidgets import QDialog
from PIL import Image, ImageQt, ImageDraw
from PySide2.QtGui import QPixmap, QPalette, QImage, QPainter, QCursor
from .capture_form_ui import Ui_CaptureForm
from PySide2.QtCore import Qt
from PySide2.QtGui import QMouseEvent, QPaintEvent, QPen, QBrush
import pyperclip
from ..util import *
from ..config import Config
import logging

class CaptureForm(QDialog):
    def __init__(self, parent_window, parent = None, logger = None):
        super(CaptureForm, self).__init__(parent)
        self.ui = Ui_CaptureForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

        self.parent_window = parent_window
        self.logger = logger if logger is not None else logging.getLogger(__name__)

        #キャプチャ位置（SetPic時に更新）
        self.basePos = (0,0)
        self.topleft = (0,0)
        self.bottomright = (0,0)
        self.isDragging = False

        # background-colorがあるとQPaletteでの画像貼り付けより優先されてしまうのでnoneに
        reset_background_color_qss = """
        QDialog {
            background-color: none;
        }
        """
        self.setStyleSheet(reset_background_color_qss)

        # self.painter = QPainter(self)
        # self.painter.begin(self)
        # pen = QPen(Qt.blue, 1.0)
        # # self.painter.setPen(pen)
        # self.painter.setBrush(Qt.blue)


    def setPicPath(self, pic_path):
        image = Image.open(pic_path)
        self.setPic(image, (0,0, image.width, image.height))

    def setPic(self, pil_image, rect):
        self.setGeometry(rect[0],rect[1],100,100)
        draw = ImageDraw.Draw(pil_image)
        #draw.ellipse((0, 0, 30, 30), outline=(255, 0, 0))
        #上線
        draw.line((0,0,pil_image.size[0],0),fill=(255,0,0),width=5)
        #右線
        draw.line((pil_image.size[0],0,pil_image.size[0],pil_image.size[1]),fill=(255,0,0),width=5)
        #下線
        draw.line((0,pil_image.size[1],pil_image.size[0],pil_image.size[1]),fill=(255,0,0),width=5)
        #左線
        draw.line((0,0,0,pil_image.size[1]),fill=(255,0,0),width=5)

        self._pastePic(pil_image)

    # PIL.Image imageをウィンドウに貼り付け　ウィンドウは画像サイズに
    def _pastePic(self, image):
        self.img = image
        self.qt_image = ImageQt.ImageQt(image)
        self.pic = QPixmap.fromImage(self.qt_image)
        self.resize(self.pic.width(), self.pic.height())
        self.pic = self.pic.scaled(self.size(), Qt.IgnoreAspectRatio)
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, self.pic)
        self.setPalette(self.palette)

    def mousePressEvent(self, event:QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.logger.debug(self.topleft)
            self.topleft = (event.pos().x(), event.pos().y())
            self.isDragging = True
        elif event.button() == Qt.RightButton:
            self.parent_window.wakeup("", "")
            self.hide()

    def mouseReleaseEvent(self, event:QMouseEvent):
        self.logger.debug(event.pos())
        self.bottomright = (event.pos().x(), event.pos().y())
        self.isDragging = False
        if not self.validClipRect(self.topleft, self.bottomright):
            msg = f"不正な選択範囲：選択範囲は左上から右下へ選択してください"
            self.logger.warning(msg)
            self.parent_window.wakeup(msg,"")
            self.hide()
            return
        cropped = self.img.crop((self.topleft[0], self.topleft[1], self.bottomright[0], self.bottomright[1]))
        try:
            ocr = OCRfromPILImage(cropped)
        except Exception as ex:
            import traceback
            traceback.print_exc()
            ocr = "OCR ERROR!!"
        #設定で有効であればクリップボードコピー
        if Config.config["copy_to_clipboard"] is True:
            pyperclip.copy(ocr)
        try:
            ja = Translate(ocr)
        except Exception as ex:
            ja = "TRANSLATE ERROR!!"
        self.parent_window.wakeup(ocr, ja)
        self.hide()

    def mouseMoveEvent(self, event:QMouseEvent):
        self.update()

    def paintEvent(self, event:QPaintEvent):
        self.painter = QPainter(self)
        pen = QPen(Qt.black, 2)
        self.painter.setPen(pen)

        pos = self.mapFromGlobal(QCursor.pos())
        mouse = (pos.x(), pos.y())

        if self.isDragging:
            w = mouse[0] - self.topleft[0]
            h = mouse[1] - self.topleft[1]

            self.painter.drawRect(self.topleft[0], self.topleft[1], w, h)
        self.painter.end()

    def validClipRect(self, topleft, bottomright):
        if bottomright[0] < topleft[0]:
            return False
        if bottomright[1] < topleft[1]:
            return False
        return True