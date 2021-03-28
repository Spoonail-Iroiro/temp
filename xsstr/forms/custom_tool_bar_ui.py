# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_tool_bar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CustomToolBar(object):
    def setupUi(self, CustomToolBar):
        if not CustomToolBar.objectName():
            CustomToolBar.setObjectName(u"CustomToolBar")
        CustomToolBar.resize(284, 70)
        self.horizontalLayout = QHBoxLayout(CustomToolBar)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnMisc = QPushButton(CustomToolBar)
        self.btnMisc.setObjectName(u"btnMisc")
        self.btnMisc.setMinimumSize(QSize(50, 50))
        self.btnMisc.setMaximumSize(QSize(50, 50))
        self.btnMisc.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout.addWidget(self.btnMisc)


        self.retranslateUi(CustomToolBar)

        QMetaObject.connectSlotsByName(CustomToolBar)
    # setupUi

    def retranslateUi(self, CustomToolBar):
        CustomToolBar.setWindowTitle(QCoreApplication.translate("CustomToolBar", u"Frame", None))
        self.btnMisc.setText(QCoreApplication.translate("CustomToolBar", u"...", None))
    # retranslateUi

