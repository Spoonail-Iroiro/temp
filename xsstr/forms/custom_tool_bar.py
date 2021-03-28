from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
import PySide2
from .custom_tool_bar_ui import Ui_CustomToolBar
from PySide2 import QtGui, QtWidgets

class CustomToolBar(QWidget):
    def __init__(self, parent_window):
        super().__init__(parent=parent_window)
        self.parent = parent_window
        self.ui = Ui_CustomToolBar()
        self.ui.setupUi(self)

    def paintEvent(self, evt):
        super().paintEvent(evt)
        opt = QtWidgets.QStyleOption()
        opt.init(self)
        p = QtGui.QPainter(self)
        s = self.style()
        s.drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, p, self)
