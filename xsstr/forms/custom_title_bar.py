from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
import PySide2
from .custom_title_bar_ui import Ui_CustomTitleBar
from PySide2 import QtGui, QtWidgets


class CustomTitleBar(QWidget):
    def __init__(self, parent_window):
        super().__init__(parent=parent_window)
        self.parent_window: QtWidgets.QMainWindow = parent_window
        self.mouse_pos = None

        self.ui = Ui_CustomTitleBar()
        self.ui.setupUi(self)

        self.ui.btnClose.clicked.connect(self.parent_window.close)
        self.ui.btnMinimize.clicked.connect(self.parent_window.showMinimized)

    def set_parent_window(self, parent):
        if self.parent_window is not None:
            self.ui.btnClose.clicked.disconnect(self.parent_window.close)
            self.ui.btnMinimize.clicked.disconnect(self.parent_window.showMinimized)

        self.parent_window = parent
        self.ui.btnClose.clicked.connect(self.parent_window.close)
        self.ui.btnMinimize.clicked.connect(self.parent_window.showMinimized)

    def mousePressEvent(self, event:PySide2.QtGui.QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.mouse_pos = event.globalPos()#event.globalPos() - self.geometry().topLeft() - self.parent_window.geometry().topLeft()
            self.window_pos = self.parent_window.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event:PySide2.QtGui.QMouseEvent):
        return
        if event.button() & Qt.MouseButton.NoButton == Qt.MouseButton.NoButton:
            if self.ui.btnClose.underMouse() or self.ui.btnMinimize.underMouse():
                event.accept()
                return

            vec = event.globalPos() - self.mouse_pos
            self.parent_window.move(self.window_pos + vec)
            event.accept()

    def paintEvent(self, evt):
        super().paintEvent(evt)
        opt = QtWidgets.QStyleOption()
        opt.init(self)
        p = QtGui.QPainter(self)
        s = self.style()
        s.drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, p, self)