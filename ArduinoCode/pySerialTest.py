#!/usr/bin/env python3

import serial
ser = serial.Serial(port='/dev/ttyACM1',
        baudrate=115200) #Check this if fail
print(ser.name)

degree = "0";


def writeToA(inDegree):
    print("Writing to servo A")
    degree = "A" + str(inDegree) + "\n"
    ser.write(degree.encode('utf-8'))
    ser.flush()
    print("done")
    return


def isFix():
    print("Checking if there is a fix")
    message = "B\n"
    ser.write(message.encode('utf-8'))
    ser.flush()
    print(str(ser.readline()))
    return

def getLocation():
    print("Getting Location")
    message = "C\n"
    ser.write(message.encode('utf-8'))
    ser.flush()
    print(str(ser.readline()))
    return


while(True):
    degree = int(input()) 
    print("You entered" + str(degree))
    writeToA(degree)
    isFix()
    getLocation();

