#modded from http://www.binarytides.com/programming-udp-sockets-in-python/
import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("socket created")
except:
    print("socket failed")

host = raw_input("ip:") 
port = 6869

while 1:
    msg = raw_input("message to send: ")
    try:
        sock.sendto(msg, (host, port))
        d = sock.recvfrom(1024)
        reply = d[0]
        addr = d[1]
        print("server: " + reply)
        if reply=="dead":
            break
    except:
        print("send or recv fucked up")
print("Your drunk, go home")
