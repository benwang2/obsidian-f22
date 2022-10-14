import socket

used_ports = []

class Record():
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def __str__(self):
        return f"[{self.name}, {self.value}, {self.type}]"

class DNS():
    def __init__(self, query_type, records_file):
        self.query_type = query_type
        self.map = {}
        self.socket = None

        for record in open(records_file, "r"):
            hostname, ip_address, record_type = record.strip().split(" ")
            self.map[hostname.lower()] = Record(hostname, ip_address, record_type)

    def resolve(self, hostname):
        pass

    def listen(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        server_binding = ('', 50007)
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

            record = self.resolve(hostname)
            if record != None:
                response = " ".join(record.name, record.value, "A", "IN")
                recipient.send(response.encode("utf-8"))

            if not received:
                break

t1 = DNS(None, "PROJ2-DNSTS1.txt")
t2 = DNS(None, "PROJ2-DNSTS2.txt")

print({k:v.__str__() for (k,v) in t2.map.items()})