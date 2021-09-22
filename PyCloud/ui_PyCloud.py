# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyCloudxrynUc.ui'
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
        self.filelist = QListWidget(self.drop)
        self.filelist.setObjectName(u"fielist")
        self.filelist.setGeometry(QRect(20, 81, 571, 181))
        self.filelist.setStyleSheet(u"hover{\n"
"color: rgb(98,114,250);\n"
"}")
        self.Downloader = QLabel(self.drop)
        self.Downloader.setObjectName(u"Downloader")
        self.Downloader.setGeometry(QRect(0, 0, 611, 101))
        self.progressBar = QProgressBar(self.drop)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 270, 601, 23))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(98,114,164);\n"
"	color: rgb(200,200,200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{	\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.42, x2:1, y2:0.443182, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(0)
        self.Info_label = QLabel(self.drop)
        self.Info_label.setObjectName(u"Info_label")
        self.Info_label.setGeometry(QRect(-10, 300, 631, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.Info_label.setFont(font1)
        self.Info_label.setStyleSheet(u"color: rgb(98,114,250);")
        self.Info_label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.Downloader.setFont(font)
        self.Downloader.setStyleSheet(u"color: rgb(254,121,199);")
        self.Downloader.setAlignment(Qt.AlignCenter)
        self.exit_button = QPushButton(self.drop)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(590, 0, 31, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        font1.setKerning(True)
        self.exit_button.setFont(font1)
        self.exit_button.setAcceptDrops(False)
        self.exit_button.setAutoFillBackground(False)
        self.exit_button.setStyleSheet(u"")
        self.exit_button.setAutoDefault(False)
        self.exit_button.setFlat(True)
        self.upload_button = QPushButton(self.drop)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setGeometry(QRect(230, 140, 161, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(17)
        self.upload_button.setFont(font2)
        self.upload_button.setStyleSheet(u"background-color: rgb(157, 0, 255);")
        self.upload_button.setFlat(False)
        self.download_button = QPushButton(self.drop)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(230, 200, 161, 41))
        self.download_button.setFont(font2)
        self.download_button.setStyleSheet(u"background-color: rgb(157, 0, 255);")
        self.download_button.setFlat(False)

        self.verticalLayout.addWidget(self.drop)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.exit_button.setDefault(False)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.Downloader.setText(QCoreApplication.translate("Main", u"<html><head/><body><p>PyCloud</p><p><br/></p></body></html>", None))
        self.exit_button.setText(QCoreApplication.translate("Main", u"\u2715", None))
        self.upload_button.setText(QCoreApplication.translate("Main", u"Upload", None))
        self.download_button.setText(QCoreApplication.translate("Main", u"Download", None))
    # retranslateUi
