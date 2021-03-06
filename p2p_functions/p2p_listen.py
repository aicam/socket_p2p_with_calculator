import threading
from .p2p_send import transfer
from .socket_binds import *
import socket
import time
def add_listener(com_sock, transfer_sock, files, hostname, com_port, transfer_port):
    data, addr = None, None
    client_sock = bind_socket_client()
    while True:
        com_sock = bind_socket_server(com_port)
        time.sleep(1)
        try:
            data, addr = com_sock.recvfrom(1024)
        except socket.error:
            com_sock.close()
            continue
        com_sock.close()
        message = data.decode('utf-8')
        if message.__contains__(hostname):
            client_sock.sendto(data, ('192.168.1.105',com_port))
            continue
        if message.__contains__('p2p_server') and not message.__contains__(hostname):
            parse_thread = threading.Thread(target=parse_message,
                                            args=(message, transfer_port, files, hostname, com_port))
            parse_thread.start()

def parse_message(msg, port, files, hostname, com_port):
    msg_args = msg.split(',')
    if msg_args[1] == 'search_for':
        print('request search for file ', msg_args[2], ' arrived')
        found_item = None
        for item in files:
            if msg_args[2].__contains__(item["name"]):
                found_item = item
                print("Host " + msg_args[3] + " asked for " + msg_args[2])
        if found_item != None:
            print("Transfer started")
            transfer(hostname,msg_args[2],found_item['path'],port, com_port)


def start_listening(com_sock, transfer_sock, files, hostname, com_port, transfer_port):
    listening_thread = threading.Thread(target=add_listener, args=(com_sock, transfer_sock, files, hostname, com_port, transfer_port),
                                        daemon= True)
    return listening_thread