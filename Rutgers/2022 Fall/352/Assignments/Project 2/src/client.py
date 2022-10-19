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

    responses = []
    with open('PROJ2-HNS.txt', 'r') as input:
        lines = input.readlines()
        for line in lines:
            print("[C]: Query",line)
            try:
                cs.send(line.strip().encode("utf-8"))
                data = cs.recv(4096).decode("utf-8")
                responses.append(data)
                print("[C]: Received",data)
            except socket.timeout as e:
                print("TIMED OUT FOR",line)
            except socket.error as e:
                print(e)

    with open("RESOLVED.txt", "w") as out:
        out.write("\n".join(responses))

    cs.close()

def main():
    client()


if __name__ == "__main__":
    main()