import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)



f = open("server.py", 'rb')
l = f.read(3)
sock.sendto(b'hello' + b'123', ("0.0.0.0", 4444))