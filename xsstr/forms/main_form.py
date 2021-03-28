import logging
from .custom_tool_bar_ui import Ui_CustomToolBar
from pathlib import Path
import keyboard
from PIL import ImageGrab
from PySide2.QtWidgets import QDialog
from PySide2 import QtCore
from PySide2.QtCore import QEvent
from PySide2.QtGui import QCloseEvent, QFocusEvent
from PySide2.QtWidgets import QApplication
from .main_form_ui import Ui_MainForm
from ..signaler import Signaler
from .dummy_form import DummyForm
from .capture_form import CaptureForm
from ..key_state_manager import get_key_state_manager
from ..config import Config
import win32con, win32api, win32gui
import ctypes.wintypes
from ctypes.wintypes import POINT

class MINMAXINFO(ctypes.Structure):
    _fields_ = [
        ("ptReserved",      POINT),
        ("ptMaxSize",       POINT),
        ("ptMaxPosition",   POINT),
        ("ptMinTrackSize",  POINT),
        ("ptMaxTrackSize",  POINT),
    ]

class MainForm(QDialog):
    def __init__(self, logger=None):
        super(MainForm, self).__init__(None)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        self._rect = QApplication.instance().desktop().availableGeometry(self)

        self.logger = logger if logger is not None else logging.getLogger(__name__)

        # 初期ウィンドウ位置を設定
        swr = Config.config["startup_window_rect"]
        self.move(swr["x"], swr["y"])
        self.resize(swr["width"], swr["height"])
        # self.setGeometry(swr["x"], swr["y"], swr["width"], swr["height"])
        self.logger.debug(f"{self.geometry()}")

        self.setWindowFlags(QtCore.Qt.Window)
        # self.setWindowFlags(QtCore.Qt.Dialog)
        # self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint)
        self.setSizeGripEnabled(True)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # ウィンドウを最前面にする設定（有効の場合）
        if Config.config["stay_on_top"] is True:
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        # ショートカットキー設定（有効の場合）
        if Config.config["hotkey_settings"]["enabled"] is True:
            keys = Config.config["hotkey_settings"]["hotkeys"]
            self.key_state_manager = get_key_state_manager(self)
            self.key_state_manager.set_hotkeys(keys)
            self.key_state_manager.hotkey_pressed.connect(self.key_state_hotkey_pressed)

        self.ui.btnStart.clicked.connect(self.btnStart_clicked)

    def key_state_hotkey_pressed(self):
        import time
        self.logger.info(f"{time.time()} hotkey pressed signal received")

        if Config.config["stay_on_top"] is True:
            self.be_active_st()
            # self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            # self.key_state_manager.hotkey_pressed.connect(self.be_active_st)
        else:
            self.be_active()
            # self.key_state_manager.hotkey_pressed.connect(self.be_active)

    # def event(self, event:QEvent) -> bool:
    #     if event.type() == QEvent.WindowActivate:
    #         self.logger.debug("activated")
    #         # # keyboard.remove_hotkey(self.key_id)
    #         # keyboard.unhook_all_hotkeys()
    #         # self.key_id = keyboard.add_hotkey(self.hot_key, self.hotkey_pressed)
    #
    #     return super(MainForm, self).event(event)

    def btnStart_clicked(self):
        self.start_capture()

    def start_capture(self):
        #configに設定されているキャプチャ範囲をキャプチャ
        cr = Config.config["capture_rect"]
        rect = (cr["x"],cr["y"],cr["width"],cr["height"])
        grab_rect = (rect[0], rect[1], rect[0]+rect[2], rect[1]+rect[3])
        self.setWindowOpacity(0.0)
        image = ImageGrab.grab(bbox=grab_rect,all_screens=True)

        self.capture_form = CaptureForm(self)
        self.capture_form.setPic(image, rect)
        self.capture_form.show()
        # self.hide()

    def wakeup(self, ocr, ja):
        if Config.config["stay_on_top"] is True:
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        self.window = self.activateWindow()
        self.raise_()
        self.ui.txtOCR.setText(ocr)
        self.ui.txtTranslate.setText(ja)
        self.setWindowOpacity(1.0)

    def be_active_st(self):
        self.logger.info(f"Activating:stay on top")
        orig_flag = self.windowFlags()
        back_flag = self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(orig_flag)
        self.activateWindow()
        self.setFocus()
        self.raise_()
        self.show()
        self.update()
        self.setWindowFlags(back_flag)
        self.activateWindow()
        self.setFocus()
        self.raise_()
        self.show()
        self.update()

        self.start_capture()

    def be_active(self):
        self.logger.info(f"Activating")
        orig_flag = self.windowFlags()
        top_flag = self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(top_flag)
        self.update()
        self.activateWindow()
        self.setFocus()
        # self.raise_()
        self.show()
        self.flags = self.setWindowFlags(orig_flag)
        self.update()
        self.activateWindow()
        self.setFocus()
        # self.raise_()
        self.show()

        self.start_capture()

    def closeEvent(self, arg__1: QCloseEvent):
        size = (self.geometry().width(), self.geometry().height())#"(self.geometry().width(), self.geometry().height())
        pos = (self.pos().x(), self.pos().y())
        self.logger.debug(f"{size}, {pos}")
        #設定で記憶ONであれば、ウィンドウクローズ時の位置を記憶
        if Config.config["save_startup_window_rect"]:
            swr = Config.config["startup_window_rect"]
            swr["x"] = pos[0]
            swr["y"] = pos[1]
            swr["width"] = size[0]
            swr["height"] = size[1]

    # def nativeEvent(self, eventType:PySide2.QtCore.QByteArray, message:int) -> typing.Tuple:
    def nativeEvent(self, eventType, message: int):
        retval, result = super().nativeEvent(eventType, message)

        if eventType == "windows_generic_MSG":
            msg = ctypes.wintypes.MSG.from_address(message.__int__())
            # # 获取鼠标移动经过时的坐标
            # x = win32api.LOWORD(msg.lParam) - self.frameGeometry().x()
            # y = win32api.HIWORD(msg.lParam) - self.frameGeometry().y()
            # # # 判断鼠标位置是否有其它控件
            # if self.childAt(x, y) != None:
            #     return retval, result
            if msg.message == win32con.WM_NCCALCSIZE:
                # 拦截不显示顶部的系统自带的边框
                return True, 0
            # if msg.message == win32con.WM_GETMINMAXINFO:
            #     print("Get MinMax")
            #     # 当窗口位置改变或者大小改变时会触发该消息
            #     info = ctypes.cast(
            #         msg.lParam, ctypes.POINTER(MINMAXINFO)).contents
            #     # 修改最大化的窗口大小为主屏幕的可用大小
            #     info.ptMaxSize.x = self._rect.width()
            #     info.ptMaxSize.y = self._rect.height()
            #     # 修改放置点的x,y坐标为0,0
            #     info.ptMaxPosition.x, info.ptMaxPosition.y = 0, 0
            if msg.message == win32con.WM_NCHITTEST:
                x = win32api.LOWORD(msg.lParam) - self.frameGeometry().x()
                y = win32api.HIWORD(msg.lParam) - self.frameGeometry().y()
                # print(f"Child:{self.childAt(x, y)}")
                # print(f"lparam：0x{format(msg.lParam, '08x')}")
                print(f"pos:({x},{y})")
                print(f"{self.frameGeometry().width()}")
                print(f"{self.width()}")
                print(f"{self.geometry().width()}")

                self.BorderWidth=5

                w, h = self.width(), self.height()
                lx = x < self.BorderWidth
                rx = x > w - self.BorderWidth
                ty = y < self.BorderWidth
                by = y > h - self.BorderWidth
                # 左上角
                if (lx and ty):
                    return True, win32con.HTTOPLEFT
                # 右下角
                if (rx and by):
                    return True, win32con.HTBOTTOMRIGHT
                # 右上角
                if (rx and ty):
                    return True, win32con.HTTOPRIGHT
                # 左下角
                if (lx and by):
                    return True, win32con.HTBOTTOMLEFT
                # 上
                if ty:
                    return True, win32con.HTTOP
                # 下
                if by:
                    return True, win32con.HTBOTTOM
                # 左
                if lx:
                    return True, win32con.HTLEFT
                # 右
                if rx:
                    return True, win32con.HTRIGHT
                # 标题
                return True, win32con.HTCAPTION
        return retval, result
        #
        # print(f"{eventType},{message}")
        #
        # rtn = super().nativeEvent(eventType, message)
        #
        # print(rtn)
        #
        # return rtn
        pass


