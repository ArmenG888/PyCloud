import socket,os,time,shutil,sys
from hurry.filesize import size
class server:
    def __init__(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        print("Server is running on Ip:"+str(ip)+" port:"+str(port))
        s.listen(5)
        self.conn, addr = s.accept()
        for i in range(2):
            message = self.conn.recv(1024).decode()
            self.message = message.split(",")
            if self.message[0] == "u":
                self.upload()
            elif self.message[0] == "d":
                self.prepare_download()
            elif self.message[0] == "l":
                self.login()
            elif self.message[0] == "r":
                self.register()

    def prepare_download(self):
        os.chdir(self.username)
        files = os.listdir()
        x = ""
        for i in files:
            x += i +" size: "+size(os.path.getsize(i))+","
        print(x)
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
        os.chdir(self.username)
        self.list_num = self.conn.recv(1024).decode()
        self.conn.send("0".encode())
        file_list = self.conn.recv(1024).decode()
        file_list = file_list.split(",")
        print(file_list)
        for i in range(len(file_list)):
            jsonString = bytearray()
            while True:
                # recieves the packet by 1024
                packet = self.conn.recv(1024)
                if not packet:
                    break
                jsonString.extend(packet)
            # writes the file
            with open(file_list[i], "wb+") as w:
                w.write(jsonString)
    def register(self):
        with open("database.csv", "a") as w:
            w.write(self.message[1] +","+self.message[2]+","+self.message[3]+"\n")
        w.close()
        os.mkdir(self.message[1])
    def login(self):
        with open("database.csv", "r") as r:
            r = r.read()
            r = r.split("\n")
        login = False
        for i in r:
            i = i.split(",")
            if i[0] == self.message[1] and i[1] == self.message[2]:
                login = True
            else:
                continue
        self.username = self.message[1]
        if login == True:
            self.conn.send("1".encode())
        else:
            self.conn.send("0".encode())
if __name__ == "__main__":
   server = server("127.0.0.1",52000)
