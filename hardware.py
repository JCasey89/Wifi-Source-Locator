#!/usr/bin/env python3

import serial
import time
ser = serial.Serial(port='/dev/ttyACM1',
        baudrate=115200) #Check this if fail
#print(ser.name)

degree = "0";


def write_to_pan(inDegree):
    degree = "A" + str(inDegree) + "\n"
    ser.write(degree.encode('utf-8'))
    ser.flush()
    time.sleep(1)
    return


def is_fixed():
    message = "B\n"
    ser.write(message.encode('utf-8'))
    ser.flush()
    returned = ser.readline()

    if(returned ==  b'0\r\n'):
        return False
    else:
        return True

def get_location():
    message = "C\n"
    ser.write(message.encode('utf-8'))
    ser.flush()
    return str(ser.readline().decode("utf-8").rstrip())


#while(True):
#    degree = int(input()) 
#    print("You entered" + str(degree))
#
#    print("Writing to servo A")
#    write_to_pan(degree);
#    print("Done!\n")
#    print("Checking if there is a fix")
#    if(is_fixed()):
#        print("\tGot a fix WOO!!!")
#    else:
#        print("\tNo fix, boo :( ")
#        
#    print("Getting Location:[" + get_location() + "]")
#
