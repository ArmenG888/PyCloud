import socket,os
from hurry.filesize import size
class server:
    def __init__(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen(5)
        self.conn, addr = s.accept()
        message = self.conn.recv(1024).decode()
        self.message = message.split(",")
        if self.message[0] == "u":
            self.upload()
        elif self.message[0] == "d":
            self.download()
    def download(self):
        files = os.listdir()
        x = ""
        for i in files:
            x += i +" size: "+size(os.path.getsize(i))+","

        self.conn.send(x.encode())
    def upload(self):
        print(self.message[1])
app = server(ip="192.168.1.2",port=52000)
