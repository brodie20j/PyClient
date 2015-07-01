__author__ = 'jonathanbrodie'


#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5701
BUFFER_SIZE = 10  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

client, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = client.recv(BUFFER_SIZE)
    if not client: break
    print("received data:", data)
    client.send(data)  # echo
client.close()