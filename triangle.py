#! /usr/bin/env python3
import math
import node
import sys

def distance(node1, node2):
    doubleDistance = 0

    return doubleDistance

    #       C
    #    b    a
    #   A   c  B
    # C = 180 - A - B
    # b = (c/sinC)*sinB
    # a = (c/sinC)*sinB 

def triangulate(node1, node2):
    boolNode1Closer = False
    node1Long = 0
    node1Lat = 0
    node2Long = 0
    node2Lat = 0


    distNode2Node = distance(node1, node2)

    intTgtAngle = 180 - node1.intServoPanDegree - node2.intServoPanDegree
    
    if (node1.intWifiStrength > node2.intWifiStrength):
        distNode2Target = calcDistNode2Target(node1, distNode2Node,\
                intTgtAngle)
        boolNode1Closer = True
    elif (node1.intWifiStrength < node2.intWifiStrength or \
            node1.intWifiStrength == node2.intWifiStrength):
        boolNode1Closer = False
        distNode2Target = calcDistNode2Target(node2, distNode2Node,\
                intTgtAngle)
    else:
        print("math error in triangulation during law of sines")
        sys.exit(1)

    if boolNode1Closer:
        finalLat = math.asin(math.sin(node1Lat)
    elif not boolNode1Closer:
        pass
    else:
        print("Error during loc calc via bearing and dist from node to tgt")
        sys.exit(1)


#    targetCoord(finalLong, finalLat)

    return targetCoord
