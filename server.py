# first of all import the socket library
import socket
import time
from protocol_functions.parse_data import parse_welcome_message, check_finished
from protocol_functions.get_params import get_params
from math_operations.call_functions import recv_data
import sys
# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything

port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    # Get data
    recv = c.recv(1024)
    status, ans = parse_welcome_message(recv)
    if status :
        c.send(bytes(ans, 'utf8'))
    else:
        c.send(b"failed connection")
        c.close()
        continue
    recv = c.recv(1024)
    while not check_finished(recv):
        try:
            start_time = time.time()
            ans = bytes(str(recv_data(get_params(recv))), 'utf8')
            end_time = time.time()
            c.send(b"answer : " + ans + b' time: ' + bytes(str(end_time - start_time), 'utf8') + b'\n')
        except Exception:
            c.close()
            break
        try:
            recv = c.recv(1024)
        except Exception:
            c.close()
            break
    try:
        c.send(b"FINISHED")
    except Exception:
        continue
    # Close the connection with the client
    try:
        c.close()
    except Exception:
        continue
