#!/usr/bin/python

from socket import *
from time import ctime

HOST = '192.168.7.38'
PROT = 59
BUFSIZ = 1024 
ADDR = (HOST,PROT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for messagess...')
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    data = data.decode()
    udpSerSock.sendto(('[%s] %s' %(ctime(), data)).encode(), addr)
    print('.....received from and return to : ',addr)

udpSerScok.close()
