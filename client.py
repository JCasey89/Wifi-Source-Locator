#! /usr/bin/env python3
#modded from http://www.binarytides.com/programming-udp-sockets-in-python/

import socket
import sys
import time

class socks(object):
    sock = None

    def __init__(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except:
            print("Socket Creation Failed")
            sys.exit(1)


    def sendNodeData(self, host, port, msg):
        
        data = False
        while not(data):
            try:
                self.sock.sendto(msg, (host, port))
                data = self.sock.recvfrom(1024)
                time.sleep(5)
            except:
                print("send or recv failed, please check server if send succeeded\
                        or failed to determin error")
                sys.exit(1)
        self.sock.close()
        print("Server Disconnected")
