import time
from .socket_binds import *
import threading

def ask_for_file(filename, sock, com_port, transfer_port, hostname):
    sock.sendto(b'p2p_server,search_for,' + filename.encode('utf8') + b',' + hostname.encode('utf8'),
                ('0.0.0.0', com_port))
    counter = 1000
    server_sock = bind_socket_server(com_port)
    while True:
        time.sleep(0.01)
        counter -= 1
        try:
            data, addr = server_sock.recvfrom(1024)
            decoded_data = data.decode('utf-8')
            if (data.decode('utf8').__contains__('search_for') and data.decode('utf8').__contains__(hostname)):
                sock.sendto(data, ('0.0.0.0', com_port))
                continue
            if decoded_data.__contains__(filename):
                index_of_end = decoded_data.find(filename)
                index_of_start = index_of_end - 2
                index_of_end -= 2
                while decoded_data[index_of_start] != ',':
                    index_of_start -= 1
                print("host " + decoded_data[index_of_start + 1:index_of_end + 1] + ' started transfer')
                write_file_thread = threading.Thread(target=write_file,args=(decoded_data[index_of_start:index_of_end], filename, bind_socket_server(transfer_port)))
                write_file_thread.start()
                break
        except:
            pass
        if counter == 0:
            break


def write_file(hostname, filename, sock):
    with open(filename, 'a+b') as f:
        while True:
            try:
                data, addr = sock.recvfrom(300)
            except socket.error:
                print("error")
                continue
            print(data, ' file data')
            decoded_data = data.decode('utf-8')
            if decoded_data.__contains__(hostname) and decoded_data.__contains__(filename):
                print(data[len(filename) + len(hostname):300])
                f.write(data[len(filename) + len(hostname):300])
            if decoded_data.__contains__(filename + 'END'):
                print('file transfered successfully')
                f.close()
                break
