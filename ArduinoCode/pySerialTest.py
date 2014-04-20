#!/usr/bin/env python3

import serial
ser = serial.Serial(port='/dev/ttyACM0',
        baudrate=9600) #Check this if fail
print(ser.name)

degree = "0";


def writeToA(inDegree):
    print("Writing to servo A")
    degree = "A" + str(inDegree) + "\n"
    ser.write(degree.encode('utf-8'))
    ser.flush()
    print("done")
    return


def writeToB(inDegree):
    print("Writing to servo B")
    degree = "B" + str(inDegree) + "\n"
    ser.write(degree.encode('utf-8'))
    ser.flush()
    print("done")
    return

while(True):
    degree = int(input()) 
    print("You entered" + str(degree))
    writeToA(degree)
    writeToB(180-degree)

