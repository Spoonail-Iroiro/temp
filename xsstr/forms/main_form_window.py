from PySide2.QtWidgets import QMainWindow
from .main_form_window_ui import Ui_MainFormWindow

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
from PySide2.QtCore import Qt

class MINMAXINFO(ctypes.Structure):
    _fields_ = [
        ("ptReserved",      POINT),
        ("ptMaxSize",       POINT),
        ("ptMaxPosition",   POINT),
        ("ptMinTrackSize",  POINT),
        ("ptMaxTrackSize",  POINT),
    ]

class MainFormWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainFormWindow, self).__init__(parent=parent)
        self.ui = Ui_MainFormWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window)

        self.ui.ctb_main.set_parent_window(self)

        self.BorderWidth = 5
        #TODO: 多分都度都度領域取り直さないといけない
        self._rect = QApplication.instance().desktop().availableGeometry(self)

        self.move(0,0)


    def nativeEvent(self, eventType, message: int):

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
            if msg.message == win32con.WM_GETMINMAXINFO:
                print("Get MinMax")
                # 当窗口位置改变或者大小改变时会触发该消息
                info = ctypes.cast(
                    msg.lParam, ctypes.POINTER(MINMAXINFO)).contents
                # 修改最大化的窗口大小为主屏幕的可用大小
                info.ptMaxSize.x = self._rect.width()
                info.ptMaxSize.y = self._rect.height()
                # 修改放置点的x,y坐标为0,0
                info.ptMaxPosition.x, info.ptMaxPosition.y = 0, 0
            if msg.message == win32con.WM_NCHITTEST:
                x = win32api.LOWORD(msg.lParam) - self.frameGeometry().x()
                y = win32api.HIWORD(msg.lParam) - self.frameGeometry().y()
                # print(f"Child:{self.childAt(x, y)}")
                # print(f"lparam：0x{format(msg.lParam, '08x')}")
                print(f"pos:({x},{y})")
                print(f"{self.frameGeometry().width()}")
                print(f"{self.width()}")
                print(f"{self.geometry().width()}")
                print(f"{self.size()}")


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
                print(self.childAt(x,y))
                if self.childAt(x,y) == self.ui.ctb_main.ui.label:
                    return True, win32con.HTCAPTION
        retval, result = super().nativeEvent(eventType, message)
        return retval, result
