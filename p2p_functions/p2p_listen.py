import threading
from .p2p_transfer import transfer
import socket

def add_listener(sock, files, hostname, transfer_port):
    data, addr = None, None
    while True:
        try:
            data, addr = sock.recvfrom(1024)
        except socket.error:
            continue
        message = data.decode('utf-8')
        if message.__contains__('p2p_server'):
            parse_message(message, transfer_port, files, hostname)

def parse_message(msg, port, files, hostname):
    msg_args = msg.split(',')
    if msg_args[1] == 'search_for':
        found_item = None
        for item in files:
            if item["name"] == msg_args[2]:
                found_item = item
                print("Host " + msg_args[3] + " asked for " + msg_args[2])
        if found_item != None:
            transfer(hostname,msg_args[2],found_item['path'],port)


def start_listening(sock, files, hostname, transfer_port):
    listening_thread = threading.Thread(target=add_listener, args=(sock, files, hostname, transfer_port))
    listening_thread.start()