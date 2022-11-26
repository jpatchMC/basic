#!/usr/bin/env python3
import socket
RHOST = '127.0.0.1'
RPORT = 5000

hfile = open("file.txt","r")
sfile = hfile.read()
print(sfile)

SND_DATA = sfile
RCV_DATA = ""

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))
print(f"send is:",(SND_DATA))
C_SOCK.send(bytearray(SND_DATA, 'utf8'))
RCV_DATA = C_SOCK.recv(1024)

print(RCV_DATA)
hfile.close()
C_SOCK.close()