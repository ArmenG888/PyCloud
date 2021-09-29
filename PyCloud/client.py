import socket,sys,time,datetime,os
from hurry.filesize import size
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_PyCloud import Ui_Main
from ui_PyCloudDownloader import Ui_Main as downloader
from ui_PyCloudLoginRegsiterWindow import Ui_Main as lrw
from ui_PyCloudLogin import Ui_Main as login_win
from ui_PyCloudRegister import Ui_Main as register_win
from ui_PyCloudUpload import Ui_Main as upload_win
class client(QMainWindow):
    def __init__(self,ip,port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        QMainWindow.__init__(self)
        self.lrw = lrw()
        self.lrw.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.lrw.pushButton.clicked.connect(self.close)
        self.lrw.login_button.clicked.connect(self.login_ui)
        self.lrw.register_button.clicked.connect(self.register_ui)
        self.show()
    def register_ui(self):
        self.register_win = register_win()
        self.register_win.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.register_win.register_button.clicked.connect(self.register)
        self.register_win.pushButton.clicked.connect(self.close)
        self.show()
    def register(self):
        username = self.register_win.username_entry.text()
        email = self.register_win.email_entry.text()
        password = self.register_win.password_entry.text()
        self.s.send("r,".encode()+username.encode()+",".encode()+password.encode()+",".encode()+email.encode())
        #self.main_window()
    def login_ui(self):
        self.login_win = login_win()
        self.login_win.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.login_win.login_button.clicked.connect(self.login)
        self.login_win.pushButton.clicked.connect(self.close)
        self.show()
    def login(self):
        username = self.login_win.username_entry.text()
        password = self.login_win.password_entry.text()
        self.s.send("l,".encode()+username.encode()+",".encode()+password.encode())
        login_bool = self.s.recv(1024).decode()
        if login_bool == "1":
            self.main_window()
    def main_window(self):
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.upload_button.clicked.connect(self.uploading_ui)
        self.ui.download_button.clicked.connect(self.downloading_ui)
        self.ui.exit_button.clicked.connect(self.close)
        self.show()
    def download(self,item):
        self.file = item.text()
        self.file = self.file.split("size:")
        self.file = self.file[0]
        # send the file that the client wants to download
        self.s.send(self.file.encode())
        # receives if it's a directory
        is_dir = self.s.recv(1024).decode()
        is_dir = True if is_dir == "0" else False
        # recieves the size of the file
        file_size = self.s.recv(1024).decode()
        file_size_con = size(int(file_size))

        # changes the file name whether its a zip file(folder) or a normal file
        if is_dir == True:
            file_1 = self.file + ".zip"
        else:
            file_1 = self.file
        jsonString = bytearray()
        mbpersecond_var = 0
        x = 0
        self.s.send("0".encode())
        # downloads by 1024
        start = time.time()
        start_time_elapsed = time.time()
        speed = "0"
        time_left = "NA"

        while True:
            # Updates all of the ui
            percentage = round(x/int(file_size)*100)
            self.downloader.progressBar.setValue(percentage)
            #self.ui.progressBar.setValue(percentage)
            self.downloader.Info_label.setText("  " + size(x) + "/" + file_size_con +"  "+ speed +" Mib/s   ETA: " + time_left)
            # recieves the packet by 1024
            packet = self.s.recv(1024)
            # counts how much data it has recieved
            mbpersecond_var += 1024
            x += 1024

            if size(mbpersecond_var) == "1M":
                mbpersecond_var = 0
                end = time.time()
                # stops the timer and resets the variable when it's 1M
                # gets the speed of the download
                speed = str(round(1/((end-start)+0.0000000000001), 1))
                # starts new timer
                start = time.time()
                # Gets the estimated time of the download
                time_ = round((int(file_size)-x) / 1000000 / float(speed))
                time_left = str(datetime.timedelta(seconds=time_))

            if not packet:
                break

            jsonString.extend(packet)
        # writes the file
        self.downloader.Info_label.setText("Writing the file...")
        with open(file_1, "wb+") as w:
            w.write(jsonString)

        end_time_elapsed = time.time()
        # calculates the time it took to download and shows it
        time_elapsed = str(datetime.timedelta(seconds=round(end_time_elapsed-start_time_elapsed)))
        self.downloader.Info_label.setText(" Time it took to download:" + time_elapsed)
        if is_dir == True:
            # extracts the zip file into a folder if the client was downloading folder
            with zipfile.ZipFile(file_1, 'r') as my_zip:
                my_zip.extractall(self.file)
            # removes the zip file
            os.remove(file_1)
        # success message
        QMessageBox.information(self, "Succes", "The file " + self.file +" has succesfully been downloaded.")
    # sets up ui for downloading
    def downloading_ui(self):

        self.downloader = downloader()
        self.downloader.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.downloader.exit_button.clicked.connect(self.close)
        self.s.send("d,".encode()+"d".encode())
        files = self.s.recv(1024).decode()
        self.available_files = files.split(",")
        for i in self.available_files:
            self.downloader.fielist.addItem(i)
        self.downloader.fielist.itemClicked.connect(self.download)
        self.show()
    def upload(self):
        # reads the file by 1024 and sends it to the client
        x = 0
        os.chdir(self.dir)
        with open(self.file,"rb") as r:
            while True:
                # reads the data by 1024
                data = r.read(1024)
                x += 1024
                print(x)
                self.s.send(data)
                if not data:break
                # sends the data
        quit()
    def uploading_ui(self):
        self.upload_win = upload_win()
        self.upload_win.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.upload_win.pushButton.clicked.connect(self.close)
        self.upload_win.progressBar.setFormat("Loading")
        self.show()
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        fileNames = dialog.selectedFiles()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            file_full_path = str(dialog.selectedFiles()[0])
        file_full_path_list = file_full_path.split("/")
        dir_list = file_full_path_list[0:-1]
        self.dir = ""
        for i in dir_list:
            self.dir += i+"/"


        self.file = file_full_path_list[-1]
        self.s.send("u,".encode()+self.file.encode())
        self.upload()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = client(ip="127.0.0.1",port=52000)
    sys.exit(app.exec_())
