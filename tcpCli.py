#!/usr/bin/python

from socket import * 
from time import ctime

HOST = '192.168.7.38'
PORT = 59
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break 
    print(data)
tcpCliSock.close()






