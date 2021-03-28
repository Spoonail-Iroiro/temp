# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
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


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(270, 554)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        font.setPointSize(9)
        MainForm.setFont(font)
        self.verticalLayout = QVBoxLayout(MainForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.ctb_main = CustomTitleBar(MainForm)
        self.ctb_main.setObjectName(u"ctb_main")
        self.ctb_main.setEnabled(True)
        self.ctb_main.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.ctb_main)

        self.tlb_main = CustomToolBar(MainForm)
        self.tlb_main.setObjectName(u"tlb_main")
        self.tlb_main.setEnabled(True)
        self.tlb_main.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.tlb_main)

        self.txtOCR = QTextEdit(MainForm)
        self.txtOCR.setObjectName(u"txtOCR")

        self.verticalLayout.addWidget(self.txtOCR)

        self.txtTranslate = QTextEdit(MainForm)
        self.txtTranslate.setObjectName(u"txtTranslate")

        self.verticalLayout.addWidget(self.txtTranslate)

        self.btnStart = QPushButton(MainForm)
        self.btnStart.setObjectName(u"btnStart")
        font1 = QFont()
        font1.setFamily(u"Meiryo UI")
        font1.setPointSize(48)
        self.btnStart.setFont(font1)

        self.verticalLayout.addWidget(self.btnStart)

        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"XSSTR", None))
        self.txtOCR.setPlaceholderText("")
        self.btnStart.setText(QCoreApplication.translate("MainForm", u"Start", None))
    # retranslateUi

