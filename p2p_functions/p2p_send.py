import socket
import threading
import time
from .socket_binds import *


def start_transfer(hostname, file, port, file_name):
    time_start = time.time()
    l = file.read(300 - len(hostname) - len(file_name))
    sock = bind_socket_client()
    while l:
        sock.sendto(hostname.encode('utf-8') + file_name.encode('utf-8') + l, ('192.168.1.105', port))
        l = file.read(300 - len(hostname) - len(file_name))
        if l == None:
            break
    sock.sendto(file_name.encode('utf-8') + b'END', ('192.168.1.105', port))
    sock.close()
    file.close()
    time_end = time.time()
    print("Transfer finished in ", (time_end - time_start), "sec")


def transfer(hostname, file_name, file_path, port, com_port):
    sock = bind_socket_client()
    sock.sendto(b'p2p_server,send_from,' + bytes(hostname, 'utf8') + b',' + bytes(file_name, 'utf8') + b',3 seconds',
                ('192.168.1.105', com_port))
    # ready = wait_for_start(sock, hostname)
    f = open(file_path, 'rb')
    transfer_thread = threading.Thread(target=start_transfer, args=(hostname, f, port, file_name))
    transfer_thread.start()
