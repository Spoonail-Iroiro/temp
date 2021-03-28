# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .custom_title_bar import CustomTitleBar
from .custom_tool_bar import CustomToolBar


class Ui_MainFormWindow(object):
    def setupUi(self, MainFormWindow):
        if not MainFormWindow.objectName():
            MainFormWindow.setObjectName(u"MainFormWindow")
        MainFormWindow.resize(287, 501)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        MainFormWindow.setFont(font)
        self.centralwidget = QWidget(MainFormWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.ctb_main = CustomTitleBar(self.centralwidget)
        self.ctb_main.setObjectName(u"ctb_main")
        self.ctb_main.setEnabled(True)
        self.ctb_main.setMinimumSize(QSize(0, 0))
        self.ctb_main.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.ctb_main)

        self.tlb_main = CustomToolBar(self.centralwidget)
        self.tlb_main.setObjectName(u"tlb_main")
        self.tlb_main.setEnabled(True)
        self.tlb_main.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.tlb_main)

        self.txtOCR = QTextEdit(self.centralwidget)
        self.txtOCR.setObjectName(u"txtOCR")

        self.verticalLayout.addWidget(self.txtOCR)

        self.txtTranslate = QTextEdit(self.centralwidget)
        self.txtTranslate.setObjectName(u"txtTranslate")

        self.verticalLayout.addWidget(self.txtTranslate)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        font1 = QFont()
        font1.setFamily(u"Meiryo UI")
        font1.setPointSize(48)
        self.btnStart.setFont(font1)

        self.verticalLayout.addWidget(self.btnStart)

        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        MainFormWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainFormWindow)

        QMetaObject.connectSlotsByName(MainFormWindow)
    # setupUi

    def retranslateUi(self, MainFormWindow):
        MainFormWindow.setWindowTitle(QCoreApplication.translate("MainFormWindow", u"MainWindow", None))
        self.txtOCR.setPlaceholderText("")
        self.btnStart.setText(QCoreApplication.translate("MainFormWindow", u"Start", None))
    # retranslateUi

