import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65431        # The port used by the server


ClientTurn = True
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    message = ''
    while True :
        if ClientTurn :
            message = input()
            if not message.__contains__('end') and len(message) > 0:
                s.sendall(message.encode())
            else:
                s.sendall(message.encode())
                ClientTurn = False
        if not ClientTurn:
            data = s.recv(1024)
            print(data)
            if str(data).__contains__('end') :
                ClientTurn = True


