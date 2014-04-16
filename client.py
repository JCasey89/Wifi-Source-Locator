#! /usr/bin/env python3
#modded from http://www.binarytides.com/programming-udp-sockets-in-python/

import socket
import sys
import time

class socks(object):
    sock = None

    def __init__(self):
        try:
            sock = socket.socket(socket.AF_INET, sock.SOCK_DGRAM)
        except:
            print("Socket Creation Failed")
            sys.exit(1)


    def sendNodeData(host, port):
        
        data = False
        while not(data):
            try:
                sock.sendto(msg, (host, port))
                data = sock.recvfrom(1024)
                reply = data[0]
                addr = data[1]
                time.sleep(5)
            except:
                print("send or recv failed, please check server if send succeeded\
                        or failed to determin error")
                sys.exit(1)
        sock.close()
        print("Server Disconnected")
