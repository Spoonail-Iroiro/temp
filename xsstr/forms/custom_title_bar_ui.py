# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_title_bar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CustomTitleBar(object):
    def setupUi(self, CustomTitleBar):
        if not CustomTitleBar.objectName():
            CustomTitleBar.setObjectName(u"CustomTitleBar")
        CustomTitleBar.resize(425, 32)
        self.horizontalLayout = QHBoxLayout(CustomTitleBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widIcon = QWidget(CustomTitleBar)
        self.widIcon.setObjectName(u"widIcon")
        self.widIcon.setMinimumSize(QSize(20, 0))
        self.widIcon.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout.addWidget(self.widIcon)

        self.label = QLabel(CustomTitleBar)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Meiryo UI")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.btnMinimize = QPushButton(CustomTitleBar)
        self.btnMinimize.setObjectName(u"btnMinimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnMinimize.sizePolicy().hasHeightForWidth())
        self.btnMinimize.setSizePolicy(sizePolicy1)
        self.btnMinimize.setMinimumSize(QSize(50, 0))
        font1 = QFont()
        font1.setPointSize(14)
        self.btnMinimize.setFont(font1)

        self.horizontalLayout.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(CustomTitleBar)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy1.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy1)
        self.btnClose.setMinimumSize(QSize(50, 0))
        self.btnClose.setFont(font1)

        self.horizontalLayout.addWidget(self.btnClose)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(CustomTitleBar)

        QMetaObject.connectSlotsByName(CustomTitleBar)
    # setupUi

    def retranslateUi(self, CustomTitleBar):
        CustomTitleBar.setWindowTitle(QCoreApplication.translate("CustomTitleBar", u"Form", None))
        self.label.setText(QCoreApplication.translate("CustomTitleBar", u"XSSTR", None))
        self.btnMinimize.setText(QCoreApplication.translate("CustomTitleBar", u"\uff0d", None))
        self.btnClose.setText(QCoreApplication.translate("CustomTitleBar", u"\u00d7", None))
    # retranslateUi

