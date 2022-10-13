from symbol import pass_stmt
import threading
import time
import socket

class Record():
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class DNS():
    def __init__(self, hostname, records):
        self.hostname = hostname
        self.map = {}
        self.socket = None

        for record in records:
            self.map[record.name] = record.value

    def listen(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        server_binding = ('', 53)
        self.socket.bind(server_binding)
        self.socket.listen(1)

        hostname = socket.gethostname()
        print("[S]: DNS host name is {}".format(hostname))
        print("[S]: Server IP address is {}".format(socket.gethostbyname(hostname)))

        csockid, addr = self.socket.accept()