import socket
import sys
from timeit import default_timer as timer
from select import select

class LoadBalancer():
    def __init__(self, lsPort, ts1HostName, ts1ListenPort, ts2HostName, ts2ListenPort):
        self.lsPort = int(lsPort)
        self.ts1HostName = ts1HostName
        self.ts1ListenPort = int(ts1ListenPort)
        self.ts2HostName = ts2HostName
        self.ts2ListenPort = int(ts2ListenPort)
    
    def __repr__(self):
        return "<LoadBalancer port='{}' ts1='{}:{}' ts2='{}:{}'>".format(self.lsPort, self.ts1HostName, self.ts1ListenPort, self.ts2HostName, self.ts2ListenPort)
    
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

        server_binding1 = ('', self.lsPort) # binding with itself
        self.socket1.bind(server_binding1)
    

        server_binding2 = (self.ts1HostName, self.ts1ListenPort)
        self.socket2.connect(server_binding2) # connecting to TS1
        # self.socket2.setblocking(0)

        server_binding3 = (self.ts2HostName, self.ts2ListenPort)
        self.socket3.connect(server_binding3) # connecting to TS2
        # self.socket3.setblocking(0)

        self.socket1.listen(1) #listening to incoming connections from client

        csockid, addr = self.socket1.accept()
        print("[LS]: Got connection to",addr)

        inputs = [self.socket2, self.socket3]
        outputs = [self.socket2, self.socket3]

        while True:
            data = csockid.recv(4096)
            url = data.decode("utf-8")
            
            print("[LS]: Resolving hostname:",url)
            record = None

            recipients = {}
            time_sent = {}

            while True:
                readable, writable, err = select(inputs, outputs, inputs)
                # print(readable, writable)

                for 

                if readable or writable:
                    for sock in writable:
                        identifier = "{}:{}".format(sock.getpeername(),sock.getsockname()[1])
                        if identifier in recipients: continue
                        print("[LS]: Forward to",sock.getpeername())
                        sock.send(url.encode("utf-8"))
                        recipients[identifier] = True
                        time_sent[identifier] = timer()

                    for sock in readable:
                        out = sock.recv(4096)
                        if not out: continue
                        record = out.decode("utf-8")
                        print("[LS]: Received data from",sock.getpeername(),":",record)
                    
                    if record:
                        break
                    
            csockid.send(record.encode("utf-8"))

def main():
    # lsListenerPort, ts1Hostname, ts1ListenPort, ts2Hostname, ts2ListenPort = sys.argv[1:]
    ls = LoadBalancer(*sys.argv[1:])
    ls.listen()

if __name__ == "__main__":
    main()