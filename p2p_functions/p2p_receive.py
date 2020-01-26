import time
from .socket_binds import *
import threading


def ask_for_file(com_sock, transfer_sock, filename, sock, com_port, transfer_port, hostname):
    sock.sendto(b'p2p_server,search_for,' + filename.encode('utf8') + b',' + hostname.encode('utf8'),
                ('192.168.1.111', com_port))
    print('p2p_server,search_for,' + filename + ',' + hostname)
    counter = 100
    while True:
        time.sleep(0.01)
        counter -= 1
        if counter == 0:
            break
        try:
            data, addr = com_sock.recvfrom(1024)
        except:
            continue
        decoded_data = data.decode('utf-8')
        # if (data.decode('utf8').__contains__('search_for') and data.decode('utf8').__contains__(hostname)):
        #     sock.sendto(data, ('192.168.1.105', com_port))
        #     continue
        if decoded_data.__contains__(filename) and not decoded_data.__contains__('search_for'):
            index_of_end = decoded_data.find(filename)
            index_of_start = index_of_end - 2
            index_of_end -= 2
            while decoded_data[index_of_start] != ',':
                index_of_start -= 1
            print("host " + decoded_data[index_of_start + 1:index_of_end + 1] + ' started transfer')
            write_file_thread = threading.Thread(target=write_file, args=(
            decoded_data[index_of_start + 1:index_of_end + 1], filename, transfer_sock))
            write_file_thread.start()
            break


def write_file(hostname, filename, sock):
    with open(filename, 'a+b') as f:
        while True:
            try:
                data, addr = sock.recvfrom(300)
            except socket.error:
                continue
            decoded_data = data.decode('utf-8')
            if decoded_data.__contains__(hostname) and decoded_data.__contains__(filename):
                f.write(data[len(filename) + len(hostname):300])
            if decoded_data.__contains__(filename + 'END'):
                print('file transfered successfully')
                print('enter command: ')
                f.close()
                break
