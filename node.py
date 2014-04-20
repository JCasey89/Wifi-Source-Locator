#! /usr/bin/env python3
import time
import antenna
import sys
#import servo

class Node(object):
    strTargetBSSID = "connected"
    strInterfaceName = ""
    intServoPanDegree = 0 #Final
    intServoTiltDegree = 0 #Final
    intWifiStrength = 0
#    intWifiPoll_epoch = 0
    strGPS_data = "gps,data,go,here"


    def __init__(self, strName):
        self.strInterfaceName = str(strName)

    def __str__(self):
        return self.strTargetBSSID + ":" + self.strInterfaceName + ":" + \
                str(self.intServoPanDegree) + ":" + str(self.intServoTiltDegree) + ":" +\
                str(self.intWifiStrength) + ":" + self.strGPS_data

    #wrapper to get signal strength
    #returns -db
    def get_strength_connected(self):
        return (int(antenna.get_strength_connected(self.strInterfaceName) * -1))

    def get_average_strength_connected(self):
        intTotalStrengths = 0
        
        for i in range(3):#0.3 second
            intTotalStrengths += self.get_strength_connected()
            time.sleep(0.1)
        intAverageStrength = int(intTotalStrengths/5)
        return intAverageStrength

    #wrapper to move the servo
    #inputs
    #   strDirection: "pan" or "tilt"
    #   intDegrees: degree to move to
    #outputs:
    #   boolSuccess
    def move(self, strDirection, intDegree):
#       input(input("Debug: %r antenna to %r degree then hit enter"\
#                 % (strDirection, intDegree))
#        print("Debug: %ring antenna to %r degrees"\
#                 % (strDirection, intDegree))
        time.sleep(1)
        return

#    def pan(intDegree):
#        raw_input("Debug: Move antenna to %r degree then hit enter"\
#                % intDegree)
#        return
#    def tilt(intDegree):
#        raw_input("Debug: Move antenna to %r degree then hit enter"\
#                % intDegree)
#        return
    def select_target(self):
        mac_strength_list = antenna.get_mac_strength_not_connected(self.strInterfaceName)
        for i in range(len(mac_strength_list)):
            print("index:%d BSSID %s: %d db" %(i,mac_strength_list[i][0],\
                    mac_strength_list[i][1]))

        target = input("Please enter the index of the target: ")
        self.strTargetBSSID = mac_strength_list[int(target)][0]
        print(self.strTargetBSSID)
        return

    def search_strength_of_target(self):
        mac_list = antenna.get_mac_strength_not_connected(self.strInterfaceName)
        for i in range(0,5):
            if self.strTargetBSSID in mac_list[i][0]:
                return mac_list[i][1]
            time.sleep(0.05)
        return (9000)

    def average_target_strength(self):
        total_strengths = 0

        for i in range(2):
            strength = self.search_strength_of_target()
            if strength == 9000:
                i = i - 1
            else:
                total_strengths = total_strengths + strength
            print("-", end="")
            sys.stdout.flush()
        average_strength = int(total_strengths/5)
        return average_strength
