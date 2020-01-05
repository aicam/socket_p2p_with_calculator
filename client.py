# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))
s.send(b"start_calculation")
command = input()
print(s.recv(1024).decode('utf8').rstrip())
while command.rstrip() != "FINISHED":
    s.send(bytes(','.join(command.split(' ')),'utf8'))
    print(s.recv(1024).decode('utf8').rstrip())
    command = input()
# close the connection
s.close()
