# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyCloudLoginRegsiterUxjELy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setEnabled(True)
        Main.resize(640, 423)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.drop = QFrame(self.centralwidget)
        self.drop.setObjectName(u"drop")
        self.drop.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56,58,89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px\n"
"}")
        self.drop.setFrameShape(QFrame.StyledPanel)
        self.drop.setFrameShadow(QFrame.Raised)
        self.Downloader = QLabel(self.drop)
        self.Downloader.setObjectName(u"Downloader")
        self.Downloader.setGeometry(QRect(0, 0, 611, 101))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.Downloader.setFont(font)
        self.Downloader.setStyleSheet(u"color: rgb(254,121,199);")
        self.Downloader.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.drop)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(590, 0, 31, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        font1.setKerning(True)
        self.pushButton.setFont(font1)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.login_button = QPushButton(self.drop)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(230, 140, 161, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(17)
        self.login_button.setFont(font2)
        self.login_button.setStyleSheet(u"background-color: rgb(157, 0, 255);color:rgb(255,255,255);")
        self.login_button.setFlat(False)
        self.register_button = QPushButton(self.drop)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(230, 200, 161, 41))
        self.register_button.setFont(font2)
        self.register_button.setStyleSheet(u"background-color: rgb(157, 0, 255);color:rgb(255,255,255);")
        self.register_button.setFlat(False)

        self.verticalLayout.addWidget(self.drop)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.Downloader.setText(QCoreApplication.translate("Main", u"<html><head/><body><p>PyCloud</p><p><br/></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Main", u"\u2715", None))
        self.login_button.setText(QCoreApplication.translate("Main", u"Login", None))
        self.register_button.setText(QCoreApplication.translate("Main", u"Register", None))
    # retranslateUi

