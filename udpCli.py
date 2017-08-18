#!/usr/bin/python

from socket import *

HOST = '192.168.7.38'
PROT = 59
BUFSIZ = 1024
ADDR = (HOST,PROT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    data = data.encode()
    udpCliSock.sendto(data,ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    data = data.decode()
    if not data:
        break
    print(data)
udpCliSock.close()
