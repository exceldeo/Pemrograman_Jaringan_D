import socket

SERVER_IP = '192.168.122.255'
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", SERVER_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print(addr)
    print("diterima ", data)
    print("dikirim oleh " , addr)