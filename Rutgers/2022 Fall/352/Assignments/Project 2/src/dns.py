import socket

class Record():
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

class DNS():
    def __init__(self, query_type, records_file):
        self.query_type = query_type
        self.map = {}
        self.socket = None

        for record in open(records_file, "r"):
            hostname, ip_address, record_type = record.split(" ")
            self.map[record.name.lower()] = Record(hostname, ip_address, record_type)

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

        dns_hostname = socket.gethostname()
        print("[S]: DNS host name is {}".format(dns_hostname))
        print("[S]: Server IP address is {}".format(socket.gethostbyname(dns_hostname)))

        recipient, _ = self.socket.accept()

        while True:
            received = self.socket.recv(4096)
            data = received.decode('utf-8').strip()
            hostname = data.lower()

            if hostname in self.map:
                record = self.map[hostname]
                response = " ".join(record.name, record.value, "A", "IN")
                recipient.send(response.encode("utf-8"))
            else:
                pass

            if not received:
                break

t1 = DNS()