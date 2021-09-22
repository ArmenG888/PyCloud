import socket,sys
from hurry.filesize import size
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_PyCloud import Ui_Main

class client(QMainWindow):
    def __init__(self,ip,port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        QMainWindow.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.upload_button.clicked.connect(self.uploading_ui)
        self.ui.download_button.clicked.connect(self.downloading_ui)
        self.ui.exit_button.clicked.connect(self.close)
        self.show()
    def download(self):
        pass
    def upload(self):
        pass
    def downloading_ui(self):
        self.ui.upload_button.deleteLater()
        self.ui.download_button.deleteLater()
        self.s.send("d,".encode())
        files = self.s.recv(1024).decode()
        self.available_files = files.split(",")
        for i in self.available_files:
            self.ui.filelist.addItem(i)
        self.ui.progressbar_ui(self)
    def uploading_ui(self):
        self.ui.upload_button.deleteLater()
        self.ui.download_button.deleteLater()
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        fileNames = dialog.selectedFiles()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            file_full_path = str(dialog.selectedFiles()[0])
            print(file_full_path)
        file_full_path_list = file_full_path.split("/")
        file_name = file_full_path_list[-1]
        self.s.send("u,".encode()+file_name.encode())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = client(ip="192.168.1.2",port=52000)
    sys.exit(app.exec_())
