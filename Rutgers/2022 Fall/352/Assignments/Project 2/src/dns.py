import socket


class Record():
    def __init__(self, name, value, type):
        self.name = name
        self.value = value

    def __repr__(self):
        return "<Record name='{}' value='{}' type='{}'>".format(self.name, self.value, self.type)

class DNS():
    def __init__(self, records):
        self.map = {}
        self.socket = None

        for record in records:
            self.map[record.name.lower()] = record

    def listen(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[S]: Server socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        server_binding = ('', 50053)
        self.socket.bind(server_binding)
        self.socket.listen(1)

        dns_hostname = socket.gethostname()
        print("[S]: DNS host name is {}".format(dns_hostname))
        print("[S]: Server IP address is {}:{}".format(socket.gethostbyname(dns_hostname),self.socket.getsockname()[1]))

        client, _ = self.socket.accept()

        while True:
            received = client.recv(4096)
            data = received.decode('utf-8').strip()
            hostname = data.lower()

            print("Resolving query:",hostname)
            if hostname in self.map:
                record = self.map[hostname]
                print(record)
                response = " ".join([record.name, record.value, "A", "IN"])
                client.send(response.encode("utf-8"))
            else:
                continue

            if received == "\0":
                print("stop")
                break

def main():
    ts1 = []
    with open("PROJ2-DNSTS1.txt","r") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            ts1.append(Record(*line))

    dns1 = DNS(ts1)
    dns1.listen()

if __name__ == "__main__":
    main()