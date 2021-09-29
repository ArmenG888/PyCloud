# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyCloudUploaduNBkKf.ui'
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
        self.title = QLabel(self.drop)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 611, 101))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(254,121,199);")
        self.title.setAlignment(Qt.AlignCenter)
        self.filelist = QListWidget(self.drop)
        self.filelist.setObjectName(u"filelist")
        self.filelist.setGeometry(QRect(20, 81, 571, 181))
        self.filelist.setStyleSheet(u"hover{\n"
"color: rgb(98,114,250);\n"
"}")
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
        self.file_add = QPushButton(self.drop)
        self.file_add.setObjectName(u"file_add")
        self.file_add.setGeometry(QRect(316, 300, 75, 23))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.file_add.setFont(font2)
        self.file_add.setAutoFillBackground(True)
        self.file_add.setStyleSheet(u"color: rgb(255,255,255);background-color:rgb(157, 0, 255);")
        self.file_add.setFlat(True)
        self.dir_add = QPushButton(self.drop)
        self.dir_add.setObjectName(u"dir_add")
        self.dir_add.setGeometry(QRect(220, 300, 91, 23))
        self.dir_add.setFont(font2)
        self.dir_add.setAutoFillBackground(True)
        self.dir_add.setStyleSheet(u"color: rgb(255,255,255);background-color:rgb(157, 0, 255);")
        self.dir_add.setFlat(True)
        self.upload = QPushButton(self.drop)
        self.upload.setObjectName(u"upload")
        self.upload.setGeometry(QRect(220, 340, 171, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        self.upload.setFont(font3)
        self.upload.setAutoFillBackground(True)
        self.upload.setStyleSheet(u"color: rgb(255,255,255);background-color:rgb(157, 0, 255);")
        self.upload.setFlat(True)
        self.progressBar = QProgressBar(self.drop)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 372, 601, 21))
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

        self.verticalLayout.addWidget(self.drop)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.exit_button.setDefault(False)
        self.file_add.setDefault(False)
        self.dir_add.setDefault(False)
        self.upload.setDefault(False)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("Main", u"<html><head/><body><p>PyCloud</p><p><br/></p></body></html>", None))
        self.exit_button.setText(QCoreApplication.translate("Main", u"\u2715", None))
        self.file_add.setText(QCoreApplication.translate("Main", u"Add a file", None))
        self.dir_add.setText(QCoreApplication.translate("Main", u"Add a Directory", None))
        self.upload.setText(QCoreApplication.translate("Main", u"Upload", None))
    # retranslateUi

