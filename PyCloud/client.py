import socket
class client:
    def __init__(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.listen(5)
