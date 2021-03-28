# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingForm(object):
    def setupUi(self, SettingForm):
        if not SettingForm.objectName():
            SettingForm.setObjectName(u"SettingForm")
        SettingForm.resize(629, 382)
        self.horizontalLayout = QHBoxLayout(SettingForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(SettingForm)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.listWidget)

        self.stackedWidget = QStackedWidget(SettingForm)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(SettingForm)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingForm)
    # setupUi

    def retranslateUi(self, SettingForm):
        SettingForm.setWindowTitle(QCoreApplication.translate("SettingForm", u"Settings", None))
    # retranslateUi

