#! /usr/bin/env python3
import time
import antenna
import sys
#import hardware

class Node(object):
    strTargetBSSID = "connected"
    strInterfaceName = ""
    intServoPanDegree = 0 #Final
#    intServoTiltDegree = 0 #Final
#    intWifiStrength = 0
#    intWifiPoll_epoch = 0
    floatLongitude = 0
    floatLatitude = 0

    def __init__(self, strName):
        self.strInterfaceName = str(strName)

    def __str__(self):
        return self.strTargetBSSID + ";" + self.strInterfaceName + ";" + \
                str(self.intServoPanDegree) + ";" + \
                str(self.floatLongitude) + ";" + str(self.floatLatitude)

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

    def move(self, strDirection, intDegree):
#        hardware.write_to_pan(intDegree)
        input("move to %d degrees" %(intDegree))
        time.sleep(1)
        return

#    def get_long_lat(self):
#        lon = hardware.getLongitude()
#        lat = hardware.getLatitude()
#        return (lon, lat)

#    def hasGPSFix(self):
#        return hardware.isFixed()


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
        for i in range(0,len(mac_list)):
            if self.strTargetBSSID == mac_list[i][0]:
                return mac_list[i][1]
            time.sleep(0.05)
        return (9000)

    def average_target_strength(self):
        total_strengths = 0

        for i in range(2):
            strength = self.search_strength_of_target()
            if strength == 9000:
                i = i - 1
                print("Looking for target")
            else:
                total_strengths = total_strengths + strength
            print(".", end="")
            sys.stdout.flush()
        average_strength = int(total_strengths/5)
        return average_strength
