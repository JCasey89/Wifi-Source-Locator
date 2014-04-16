#! /usr/bin/env python3

import node
import sys

def Search_Step(nodeTracker, intWorkingRange, strDirection, \
        intLowerReadPosition, intLowerReadStrength,\
        intHigherReadPosition, intHigherReadStrength,\
        boolLower, boolConnected):
    boolWasSame = False
    #binary search based off signal strengths
    if (intLowerReadStrength > intHigherReadStrength):
        intHigherReadPosition = int(intHigherReadPosition - intWorkingRange)
        boolLower = True
    elif (intHigherReadStrength > intLowerReadStrength):
        intLowerReadPosition = int(intLowerReadPosition + intWorkingRange)
        boolLower = False
    elif (boolLower and (intHigherReadStrength == intLowerReadStrength)):
        print("twitching LowerReadPosition")
        intWorkingRange = intWorkingRange - 1
        intLowerReadPosition = intLowerReadPosition + 2
        boolLower = True
        boolWasSame = True
    elif (not(boolLower) and (intHigherReadStrength == intLowerReadStrength)):
        print("twitching HigherReadPosition")
        intWorkingRange = intWorkingRange- 1
        intHigherReadPosition = intHigherReadPosition - 2
        boolLower = False
        boolWasSame = True
    else:
        print("Something bad happened during the search")
        sys.exit(1)
   
    print("Before Updated Strength")
    print("intLowerReadStrength = %d"%(intLowerReadStrength))
    print("intHigherReadStrength = %d"%(intHigherReadStrength))
    if (boolLower and boolWasSame):
        nodeTracker.move(strDirection, intLowerReadPosition)
        if (boolConnected):
            intLowerReadStrength = nodeTracker.get_average_strength_connected()
        else:
            intLowerReadStrength = nodeTracker.average_target_strength()
        print("After Updated Strength")
        print("intLowerReadStrength = %d ***"%(intLowerReadStrength))
        print("intHigherReadStrength = %d"%(intHigherReadStrength))
    elif (boolLower and not(boolWasSame)):
        nodeTracker.move(strDirection, intHigherReadPosition)
        if (boolConnected):
            intHigherReadStrength = nodeTracker.get_average_strength_connected()
        else:
            intHigherReadStrength = nodeTracker.average_target_strength()
        print("After Updated Strength")
        print("intLowerReadStrength = %d"%(intLowerReadStrength))
        print("intHigherReadStrength = %d ***"%(intHigherReadStrength))
    elif(not(boolLower) and not(boolWasSame)):
        nodeTracker.move(strDirection, intLowerReadPosition)
        if (boolConnected):
            intLowerReadStrength = nodeTracker.get_average_strength_connected()
        else:
            intLowerReadStrength = nodeTracker.average_target_strength()
        print("After Updated Strength")
        print("intLowerReadStrength = %d ***"%(intLowerReadStrength))
        print("intHigherReadStrength = %d"%(intHigherReadStrength))
    elif(not(boolLower) and boolWasSame):
        nodeTracker.move(strDirection, intHigherReadPosition)
        if (boolConnected):
            intHigherReadStrength = nodeTracker.get_average_strength_connected()
        else:
            intHigherReadStrength = nodeTracker.average_target_strength()
        print("After Updated Strength")
        print("intLowerReadStrength = %d"%(intLowerReadStrength))
        print("intHigherReadStrength = %d ***"%(intHigherReadStrength))
    else:
        print("error in step_search()")
    

    if not(boolWasSame):
        intWorkingRange = int(intWorkingRange/2)

    
    return (nodeTracker, intWorkingRange, strDirection, \
            intLowerReadPosition, intHigherReadPosition, boolLower,\
            intLowerReadStrength, intHigherReadStrength)




#Search 1 direction at a time
def Search1(nodeTracker, strDirection, boolConnected):

    intHigherReadStrength = 0
    intHigherReadPosition = 180
    intLowerReadStrenth = 0
    intLowerReadPosition = 0
    intWorkingRange = intHigherReadPosition - intLowerReadPosition
    boolLooking = True
    
    #get signal strengths from current max and min degrees
    nodeTracker.move(strDirection, intLowerReadPosition) #not implimented yet
    if boolConnected:
        intLowerReadStrength = nodeTracker.get_average_strength_connected()
    else:
        intLowerReadStrength = nodeTracker.average_target_strength()
    nodeTracker.move(strDirection, intHigherReadPosition) #not implimented yet
    if boolConnected:
        intHigherReadStrength = nodeTracker.get_average_strength_connected()
    else:
        intHigherReadStrength = nodeTracker.average_target_strength()
    boolLower = False
    intWorkingRange = int(intWorkingRange/2)
    print("Initial Higher Position Strength = %d" %(intHigherReadStrength))
    print("Initial Lower Position Strength = %d" %(intLowerReadStrength))
    while(boolLooking):
        
        if (intWorkingRange<2):
            boolLooking = False
            break
        step = Search_Step(nodeTracker, intWorkingRange, strDirection, \
                intLowerReadPosition, intLowerReadStrength,\
                intHigherReadPosition, intHigherReadStrength,\
                boolLower, boolConnected)
        nodeTracker = step[0]
        intWorkingRange = step[1]
        intLowerReadPosition = step[3]
        intHigherReadPosition = step[4]
        boolLower = step[5]
        intLowerReadStrength = step[6]
        intHigherReadStrength = step[7]

    #return the half-way point of the final angles
    intFinalDegree = int(((intHigherReadPosition-intLowerReadPosition)/2+ \
            intLowerReadPosition))
    nodeTracker.move(strDirection, intFinalDegree)
    if boolConnected:
        intFinalStrength = nodeTracker.get_average_strength_connected()
    else:
        intFinalStrength = nodeTracker.average_target_strength()


    if (intFinalDegree > 150):
        intFinalDegree = 150
    elif (intFinalDegree < 30):
        intFinalDegree = 30

    if (strDirection == "pan"):
        nodeTracker.intServoPanDegree = intFinalDegree
    elif (strDirection == "tilt"):
        nodeTracker.intServoTiltDegree = intFinalDegree
    nodeTracker.intWifiStrength = intFinalStrength

    return (nodeTracker)



#Alternate Pan and Tilt during Search
def Search2(nodeTracker, boolConnected):
    
    boolLooking = True

    #initialize Pan values
    intHigherReadStrengthPan = 0
    intHigherReadPositionPan = 180
    intLowerReadStrengthPan = 0
    intLowerReadPositionPan = 0
    intWorkingRangePan = intHigherReadPositionPan - intLowerReadPositionPan
    
    #initialize Pan values
    intHigherReadStrengthTilt = 0
    intHigherReadPositionTilt = 180
    intLowerReadStrengthTilt = 0
    intLowerReadPositionTilt = 0
    intWorkingRangeTilt = intHigherReadPositionTilt - intLowerReadPositionTilt
    
    
    #get values for Pan varaibles
    strDirection = "pan"
    nodeTracker.move(strDirection, intLowerReadPositionPan) #not implimented yet
    if boolConnected:
        intLowerReadStrengthPan = nodeTracker.get_average_strength_connected()
    else:
        intLowerReadStrengthPan = nodeTracker.average_target_strength()
    nodeTracker.move(strDirection, intHigherReadPositionPan) #not implimented yet
    if boolConnected:
        intHigherReadStrengthPan = nodeTracker.get_average_strength_connected()
    else:
        intHigherReadStrengthPan = nodeTracker.average_target_strength()

    boolLowerPan = False
    intWorkingRangePan = intWorkingRangePan/2

    #get values for Tilt varaibles
    strDirection = "tilt"
    nodeTracker.move(strDirection, intLowerReadPositionTilt) #not implimented yet
    if boolConnected:
        intLowerReadStrengthTilt = nodeTracker.get_average_strength_connected()
    else:
        intLowerReadStrengthTilt = nodeTracker.average_target_strength()
    nodeTracker.move(strDirection, intHigherReadPositionTilt) #not implimented yet
    if boolConnected:
        intHigherReadStrengthTilt = nodeTracker.get_average_strength_connected()
    else:
        intHigherReadStrengthTilt = nodeTracker.average_target_strength()
    boolLowerTilt = False
    intWorkingRangeTilt = intWorkingRangeTilt/2

    strDirection = "pan"
    while(boolLooking):
        
        if (intWorkingRangePan<2 and intWorkingRangeTilt<2):
            boolLooking = False
            break
        if (strDirection == "pan"):
            step = Search_Step(nodeTracker, intWorkingRangePan, strDirection, \
                    intLowerReadPositionPan, intLowerReadStrengthPan,\
                    intHigherReadPositionPan, intHigherReadStrengthPan,\
                    boolLowerPan, boolConnected)
            nodeTracker = step[0]
            intWorkingRangePan = step[1]
            intLowerReadPositionPan = step[3]
            intHigherReadPositionPan = step[4]
            boolLowerPan = step[5]
            intLowerReadStrengthPan = step[6]
            intHigherReadStrengthPan = step[7]
            strDirection = "tilt"
        elif(strDirection == "tilt"):
            step = Search_Step(nodeTracker, intWorkingRangeTilt, strDirection, \
                    intLowerReadPositionTilt, intLowerReadStrengthTilt,\
                    intHigherReadPositionTilt, intHigherReadStrengthTilt,\
                    boolLowerPan, boolConnected)
            nodeTracker = step[0]
            intWorkingRangeTilt = step[1]
            intLowerReadPositionTilt = step[3]
            intHigherReadPositionTilt = step[4]
            boolLowerTilt = step[5]
            intLowerReadStrengthTilt = step[6]
            intHigherReadStengthTilt = step[7]
            strDirection = "pan"
        else:
            print("Error in Search2 whileloop")
            sys.exit(1)



    #return the half-way point of the final angles
    strDirection = "pan"
    intFinalDegreePan = int(((intHigherReadPositionPan-intLowerReadPositionPan)/2+ \
            intLowerReadPositionPan))
    nodeTracker.move(strDirection, intFinalDegreePan)

    strDirection = "tilt"
    intFinalDegreeTilt = int(((intHigherReadPositionTilt-intLowerReadPositionTilt)/2+ \
            intLowerReadPositionTilt))
    nodeTracker.move(strDirection, intFinalDegreeTilt)

    if boolConnected:
        intFinalStrength = nodeTracker.get_average_strength_connected()
    else:
        intFinalStrength = nodeTracker.average_target_strength()
    
    if (intFinalDegreePan > 150):
        intFinalDegreePan = 150
    elif (intFinalDegreePan < 30):
        intFinalDegreePan = 30

    if (intFinalDegreeTilt > 150):
        intFinalDegreeTilt = 150
    elif (intFinalDegreeTilt < 30):
        intFinalDegreeTilt = 30

    nodeTracker.intServoPanDegree = intFinalDegreePan
    nodeTracker.intServoTiltDegree = intFinalDegreeTilt

    nodeTracker.intWifiStrength = intFinalStrength
    return (nodeTracker)
