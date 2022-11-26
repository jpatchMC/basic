#!/usr/bin/env python3
import socket
# josh patch chat send
send = input('say something:')
RHOST = '127.0.0.1'
RPORT = 5000
#SND_DATA = b'E1 ni\xc3\xb1o'

SND_DATA = send
RCV_DATA = ""

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))
#C_SOCK.send(SND_DATA)
C_SOCK.send(bytearray(SND_DATA, 'utf8'))
### turns text into a byte array
RCV_DATA = C_SOCK.recv(1024)
#print(RCV_DATA.decode())
print(RCV_DATA)
C_SOCK.close()