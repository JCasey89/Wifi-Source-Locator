#! /usr/bin/env python3
#modded from http://www.binarytides.com/programming-udp-sockets-in-python/
import socket
import sys
import triangle
import node
HOST = ''
PORT = 6869

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("socket created")
except:
    print("socket failed")
    sys.exit(1)

try:
    sock.bind((HOST, PORT))
    print("bind complete")
except:
    print("bind failed")
    sys.exit(1)

isIn = False
nodeFile = open("nodeFile",mode="w")
nodeData = []

while 1:
    d = sock.recvfrom(4096)
    data = d[0]
    addr = d[1]
    if ((not data) or (data.decode()=="kill")):
        msg = "terminating"
        msg = msg.encode()
        sock.sendto(msg, addr)
        break
    reply = "recieved"
    sock.sendto(reply.encode(), addr)
    #string slice from [2:len(data.strip())+2 to remove the preceding b'
    #  and the trailing '
    print("Message[" +str(addr[0]) + ":" + str(addr[1])+ '] - ' +\
            str(data.strip())[2:(len(data.strip())+2)])
    for i in range(0,len(nodeData)):
        if addr in nodeData[i]:
            nodeData[i].append(data.strip())
            isIn = True
        else:
            isIn = False
    if not isIn:
        nodeData.append([addr, data.strip()])
sock.close()

#WARNING: Assuming that the server recieves 2 node messages from seperate IP
#   addresses
for i in range(0,len(nodeData)):
    nodeData[i][0] = str(nodeData[i][0][0])
    nodeData[i][1] = str(nodeData[i][1])[2:len(nodeData[i][1])+2]

nodeFile.write(str(nodeData))

node1Data = nodeData[0][1].split(";")

node1 = node.Node(node1Data[1])
node1.strTargetBSSID = node1Data[0]
node1.intServoPanDegree = int(node1Data[2])
node1.floatLongitude = float(node1Data[3])
node1.floatLatitude = float(node1Data[4])

node2Data = nodeData[1][1].split(";")

node2 = node.Node(node2Data[1])
node2.strTargetBSSID = node2Data[0]
node2.intServoPanDegree = int(node2Data[2])
node2.floatLongitude = float(node2Data[3])
node2.floatLatitude = float(node2Data[4])

print(node1)
print(node2)

#set arg1 to east node
if (node1.floatLongitude > node2.floatLongitude):
    target = triangle.triangulate(node1, node2)
elif (node1.floatLongitude < node2.floatLongitude):
    target = triangle.triangulate(node2, node1)
elif (node1.floatLongitude == node2.floatLongitude):
    if ((node1.floatLatitude != node2.floatLatitude) and \
            (node1.intServoPanDegree != 90) or (node2.intServoPanDegree != 90)):
        target = triangle.triangulate(node1, node2)
    else:
        print("Unable to form a triangle for triangulation")
        sys.exit(1)
else:
    print("Error: unable to triangulate")
    sys.exit(1)

print("Target Longitude,Latitude: ", end="")
print(target)
nodeFile.write(str(target))
nodeFile.close()
