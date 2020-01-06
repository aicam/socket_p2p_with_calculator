import socket
import threading
import time

def bind_socket(port):
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM,
                         socket.IPPROTO_UDP)  # UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.bind(('0.0.0.0', port))
    sock.setblocking(0)
    return sock

def start_transfer(sock, hostname, file, port, file_name):
    time.sleep(3)
    l = file.read(300)
    while l:
        sock.sendto(hostname.encode('utf-8') + file_name.encode('utf-8') + l, ('0.0.0.0', port))
        l = file.read(300)
    sock.sendto(hostname.encode('utf-8') + b'END', ('0.0.0.0', port))
    file.close()

def transfer(hostname, file_name, file_path, port):
    sock = bind_socket(port)
    file_object = open(file_path, "rb")
    sock.sendto(b'p2p_server,send_from,' + bytes(hostname,'utf8') + b',' + bytes(file_name,'utf8') + b',3 seconds',
                ('0.0.0.0',port))
    # ready = wait_for_start(sock, hostname)
    f = open(file_path, 'rb')
    transfer_thread = threading.Thread(target=start_transfer,args=(sock, hostname, f, port, file_name ))
    transfer_thread.start()