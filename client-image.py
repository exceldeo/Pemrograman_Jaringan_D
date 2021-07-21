import sys
import socket

# Server Address
ipserv = ['192.168.122.63', '192.168.122.198']

count = 0
for i in ipserv:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (i, 10000)
        print(f"connecting to {server_address}")
        sock.connect(server_address)


        try:
                # Send data
                img = "Topologi.png"
                imgfile = open(img, 'rb')
                imgbytes = imgfile.read()
                print(f"sending {img}")
                sock.sendall(imgbytes)
                # Look for the response
                amount_received = 0
                amount_expected = len(imgbytes)
                count += 1
                img_recv = "image-received-alpine" + str(count) + ".png"
                with open(img_recv, 'wb') as file:
                    while amount_received < amount_expected:
                        data = sock.recv(16)
                        amount_received += len(data)
                        if not data:
                            break
                        file.write(data)
        finally:
                print(f"{img_recv} received")
                print("closing")
                sock.close()