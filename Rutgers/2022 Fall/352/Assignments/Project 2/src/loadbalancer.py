import socket
from select import select

class LoadBalancer():
    def _init_(self, ts1HostName, ts1ListenPort, ts2HostName, ts2ListenPort):
       self.ts1HostName = ts1HostName
       self.ts1ListenPort = ts1ListenPort
       self.ts2HostName = ts2HostName
       self.ts2ListenPort = ts2ListenPort

    
    def listen(self):
        try:        # Socket 1
            self.socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit

        try:        # Socket 2
            self.socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit

        try:        # Socket 3
            self.socket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit

        server_binding1 = ('', 50000) # binding with itself
        self.socket1.bind(server_binding1)
        server_binding2 = (self.ts1HostName, self.ts1ListenPort)
        server_binding3 = (self.ts2HostName, self.ts2ListenPort)
        self.socket2.connect(server_binding2) # connecting to TS1
        self.socket3.connect(server_binding3) # connecting to TS2

        self.socket1.listen(1) #listening to incoming connections from client

        csockid, addr = self.socket1.accept()

        while True:
            readable, writable, err = select([self.socket2, self.socket3], [], [], 7)

            url = csockid.recv(4096).decode("utf-8")
            if readable or writable:
                for socket in writable:
                    socket.send(url.encode("utf-8"))
