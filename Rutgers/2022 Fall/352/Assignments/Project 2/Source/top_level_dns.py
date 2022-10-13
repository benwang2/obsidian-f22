from symbol import pass_stmt
import threading
import time
import socket

class Record():
    def __init__(self):
        pass

class DNS():
    def __init__(self, records):
        pass

def ts1():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 53)
    ss.bind(server_binding)
    ss.listen(1)