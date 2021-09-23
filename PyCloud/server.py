import socket,os,time
from hurry.filesize import size
class server:
    def __init__(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen(5)
        self.conn, addr = s.accept()
        while True:
            message = self.conn.recv(1024).decode()
            self.message = message.split(",")
            if self.message[0] == "u":
                self.upload()
            elif self.message[0] == "d":
                self.prepare_download()
    def prepare_download(self):
        files = os.listdir()
        x = ""
        for i in files:
            x += i +" size: "+size(os.path.getsize(i))+","

        self.conn.send(x.encode())
        # receives the name of the file and sends back the size of it
        file = self.conn.recv(1024).decode()

        # checks if is it folder or a file
        a = os.path.isdir(file)
        self.is_dir = "0" if a == True else "1"
        # if its a folder it makes the folder a zip file to send it
        if self.is_dir == "0":
            shutil.make_archive(file, 'zip',file)
            file += ".zip"
        # sends is it a folder or a file to the client
        self.conn.send(self.is_dir.encode())
        # sends the size of the file or folder
        self.file_size = os.path.getsize(file)
        self.conn.send(str(self.file_size).encode())
        # Calls the download function
        self.conn.recv(1024)
        self.download(file)
    def download(self,file):
        # reads the file by 1024 and sends it to the client
        with open(file,"rb") as r:
            while True:
                # reads the data by 1024
                data = r.read(1024)
                if not data:break
                # sends the data
                self.conn.send(data)
    def upload(self):
        self.file = self.message[1]
        self.conn.send("0".encode())
        jsonString = bytearray()
        while True:
            # recieves the packet by 1024
            packet = self.conn.recv(1024)
            if not packet:
                break
            jsonString.extend(packet)
        # writes the file
        with open(self.file, "wb+") as w:
            w.write(jsonString)

app = server(ip="192.168.1.2",port=52000)
