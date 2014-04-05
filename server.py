#modded from http://www.binarytides.com/programming-udp-sockets-in-python/
import socket


HOST = ''
PORT = 6869

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("socket created")
except:
    print("socket failed")

try:
    sock.bind((HOST, PORT))
    print("bind complete")
except:
    print("bind failed")

isIn = False
nodeFile = open("nodeFile",mode="w")
nodeData = [[]]
while 1:
    d = sock.recvfrom(4096)
    data = d[0]
    addr = d[1]
    if ((not data) or (data=="kill")):
        if len(nodeData) > 1:
            for i in range(1,len(nodeData)):
                sock.sendto("dead", nodeData[i][0])
        break
    reply = "recieved: " + data
    sock.sendto(reply, addr)
    print("Message[" +addr[0] + ":" + str(addr[1])+ '] - ' + data.strip())
    for i in range(0,len(nodeData)):
        if addr in nodeData[i]:
            nodeData[i].append(data.strip())
            isIn = True
        else:
            isIn = False
    if not isIn:
        nodeData.append([addr, data.strip()])
sock.close()
nodeFile.write(str(nodeData))
nodeFile.close()
