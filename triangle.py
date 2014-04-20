#! /usr/bin/env python3
import math
import node
import sys

def distance(y, x):
    
    return math.sqrt((x*x) + (y*y))


    return c

    #       C
    #    b    a
    #   A   c  B
    # C = 180 - A - B
    # a = (c/sinC)*sinA 
    # node2 = A
    # node1 = B
    
def triangulate(node1, node2):
    boolNode1Closer = False
    node1Long = node1.floatLongitude
    node1Lat = node1.floatLatitude
    node2Long = node2.floatLongitude
    node2Lat = node2.floatLatitude
    
    angle_B = math.radians(node1.intServoPanDegree) - \
            math.atan(abs(node1Lat - node2Lat)/abs(node1Long - node2Long))
    
    angle_A = math.radians(180 - node2.intServoPanDegree) - \
            math.atan(abs(node1Lat - node2Lat)/abs(node1Long - node2Long))

    side_c = distance(node1Lat - node2Lat, node1Long - node2Long)

    angle_C = math.radians(180 - math.degrees(node1_angle_rad) -\
            math.degrees(node2_angle_rad))
    
    side_a = (side_c/math.sin(angle_C))*math.sin(angle_A)
    side_b = (side_c/math.sin(angle_C))*math.sin(angle_B)

    #from node 1(B)
    longDif = math.cos(angle_B)*side_a
    latDif = math.sin(angle_B)*side_a
    
    if (node1.intServoPanDegree < 90) :
        finalLong = node1Long - longDif
        finalLat = node1Lat + latDif
    elif(node1.intServoPanDegree > 90):
        finalLong = node1Long + longDif
        finalLat = node1Lat + latDif
    elif(node1.intServoPanDegree == 90):
        finalLong = node1Long
        finalLat = node1Lat + latDif
    else:
        print("error during trianglation")
        sys.exit(1)
    
    targetCoord = (finalLong, finalLat)

    return targetCoord
