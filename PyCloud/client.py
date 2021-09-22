import socket,sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_PyCloud import Ui_Main

class client(QMainWindow):
    def __init__(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        QMainWindow.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.upload_button.clicked.connect(self.upload)
        self.download_button.clicked.connect(self.download)
        self.ui.exit_button.clicked.connect(self.close)
        self.show()
    def download(self):
        pass
    def upload(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = client(ip="192.168.1.2",port=52000)
    sys.exit(app.exec_())
