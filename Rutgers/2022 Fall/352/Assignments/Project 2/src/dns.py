import socket
import sys

class Record():
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def __repr__(self):
        return "<Record name='{}' value='{}' type='{}'>".format(self.name, self.value, self.type)

class DNS():
    def __init__(self, records, port):
        self.map = {}
        self.socket = None
        self.port = port

        for record in records:
            self.map[record.name.lower()] = record

    def listen(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        server_binding = ('', self.port)
        self.socket.bind(server_binding)
        self.socket.listen(1)

        dns_hostname = socket.gethostname()
        print("[S]: DNS host name is {}".format(dns_hostname))
        print("[S]: Server IP address is {}:{}".format(socket.gethostbyname(dns_hostname),self.socket.getsockname()[1]))

        client, _ = self.socket.accept()
        print("[S]: Established connection with",client.getpeername())

        while True:
            received = client.recv(4096)

            if not received: break

            data = received.decode('utf-8').strip()

            hostname = data.lower()

            print("Resolving query:",hostname,"=",hostname in self.map)
            if hostname in self.map:
                record = self.map[hostname]
                response = " ".join([record.name, record.value, "A", "IN"])
                client.send(response.encode("utf-8"))
                
                received = None
                data = None
            else:
                continue