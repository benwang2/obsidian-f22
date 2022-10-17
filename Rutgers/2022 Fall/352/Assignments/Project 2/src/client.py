import sys
import socket

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    
    lsHostName, lsListenPort = sys.argv[1], int(sys.argv[2])
    server_binding = (lsHostName, lsListenPort)
    cs.connect(server_binding)

    with open("RESOLVED.txt", "w") as out:
        with open('PROJ2-HNS.txt', 'r') as input:
            lines = input.readlines()
            for line in lines:
                try:
                    cs.send(line.strip().encode("utf-8"))
                    data = cs.recv(100).decode("utf-8")
                    out.write(data)
                except socket.timeout as e:
                    print("TIMED OUT FOR",line)
                except socket.error as e:
                    print(e)

            cs.send("\0")
        out.close()

    cs.close()

def main():
    client()


if __name__ == "__main__":
    main()