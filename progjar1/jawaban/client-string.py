import sys
import socket
import random
import string

# Server Address
ipserv = ['192.168.122.63', '192.168.122.198']

for i in ipserv:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (i, 10000)
        print(f"connecting to {server_address}")
        sock.connect(server_address)


        try:
                # Send data
                # Change N from 100 to 2000000 (2mb)
                N = 100 
                message = ''.join(random.choices(string.ascii_uppercase, k = N))
                print(f"sending {message}")
                sock.sendall(message.encode())
                # Look for the response
                amount_received = 0
                amount_expected = len(message)
                while amount_received < amount_expected:
                    data = sock.recv(16)
                    amount_received += len(data)
                    print(f"{data}")
        finally:
                print("closing")
                sock.close()