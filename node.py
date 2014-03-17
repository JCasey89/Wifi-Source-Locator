import time
import antenna
#import servo

class Node(object):
    strTargetBSSID = ""
    strInterfaceName = ""
    intServoPanDegree = 0 #Final
    intServoTiltDegree = 0 #Final
    intWifiStrength = 0
    intWifiPoll_epoch = 0
    intGPS_epoch = 0
    floatGPS_Longitude_degree = 0.0
    floatGPS_Longitude_minute = 0.0
    floatGPS_Latitude_degree = 0.0
    floatGPS_Latitude_minute = 0.0
    floatAltitude_cm = 0.0
    
    def __init__(self, strName):
        self.strInterfaceName = str(strName)

    #wrapper to get signal strength
    #returns -db
    def get_strength_connected(self):
        return (int(antenna.get_strength_connected(self.strInterfaceName) * -1))

    def get_average_strength_connected(self):
        intTotalStrengths = 0
        
        for i in range(5):#1 second debounce
            intTotalStrengths += self.get_strength_connected()
            time.sleep(0.2)
        intAverageStrength = int(intTotalStrengths/5)
        return intAverageStrength

    #wrapper to move the servo
    #inputs
    #   strDirection: "pan" or "tilt"
    #   intDegrees: degree to move to
    #outputs:
    #   boolSuccess
    def move(self, strDirection, intDegree):
        input("Debug: %r antenna to %r degree then hit enter"\
                 % (strDirection, intDegree))
        return

#    def pan(intDegree):
#        raw_input("Debug: Move antenna to %r degree then hit enter"\
#                % intDegree)
#        return
#    def tilt(intDegree):
#        raw_input("Debug: Move antenna to %r degree then hit enter"\
#                % intDegree)
#        return
