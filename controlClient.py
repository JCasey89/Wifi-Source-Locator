#! /usr/bin/env python3
#modded from http://www.binarytides.com/programming-udp-sockets-in-python/

import socket
import sys
import time

host = input("please enter the ip address of the server: ")
port = int(input("please enter the port number on the server: "))

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print("Socket Creation Failed")
    sys.exit(1)

msg = ""
while msg != "kill":
    msg = input("Please enter \"kill\" to terminate the server: ")

msg = msg.encode()
try:
    sock.sendto(msg, (host, port))
    sock.recvfrom(1024)
except socket.error:
        print("send or recv failed, please check server if send" +\
                " succeded or failed to determine error")
        sys.exit(1)
sock.close()
print("Server Disconnected")
