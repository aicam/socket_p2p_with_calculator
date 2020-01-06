import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)  # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.bind(('0.0.0.0', UDP_PORT))
sock.setblocking(0)
sock.sendto("hello world".encode('utf-8'), ("0.0.0.0", 5005))
while True:
    try:
        data, addr = sock.recvfrom(len(b'hello') + 3)  # buffer size is 1024 bytes
        print(data[0:4])
        print(data[4:6])
    except socket.error:
        pass
