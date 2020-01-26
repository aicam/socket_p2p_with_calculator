import socket

def bind_socket_server(port):
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM,
                         socket.IPPROTO_UDP)  # UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.bind(('192.168.1.105', port))
    sock.setblocking(0)
    return sock

def bind_socket_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20)
    return sock