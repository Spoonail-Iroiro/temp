from PySide2.QtCore import QObject, Signal

class Signaler(QObject):
    hotkey_pressed = Signal()
    def __init__(self, parent):
        super().__init__(parent)

