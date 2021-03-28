from PySide2.QtWidgets import QDialog
from PySide2 import QtCore
from .main_form_ui import Ui_MainForm
from ..signaler import Signaler
import keyboard

class DummyForm(QDialog):
    def __init__(self, parent):
        super(DummyForm, self).__init__(parent)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        self.ui.txtOCR.setText("Dymmy")


