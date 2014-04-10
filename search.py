
import node
import sys

def Search_Step(nodeTracker, intWorkingRange, strDirection, \
        intLowerReadPosition, intLowerReadStrength,\
        intHigherReadPosition, intHigherReadStrength,\
        boolLower):
    #binary search based off signal strengths
    if (intLowerReadStrength > intHigherReadStrength):
        intHigherReadPosition = int(intHigherReadPosition - intWorkingRange)
        boolLower = True

    elif (intHigherReadStrength > intLowerReadStrength):
        intLowerReadPosition = int(intLowerReadPosition + intWorkingRange)
        boolLower = False
    elif (boolLower):
        intWorkingRange =- 1
        intLowerReadPosition = intLowerReadPosition - 2
    elif (not(boolLower)):
        intWorkingRange =- 1
        intHigherReadPosition = intHigherReadPosition - 2
    else:
        print("Something bad happened during the search")
        sys.exit(1)
    if (boolLower):
        nodeTracker.move(strDirection, intHigherReadPosition)
        intHigherReadStrength = nodeTracker.get_average_strength_connected()
    else:
        nodeTracker.move(strDirection, intLowerReadPosition)
        intLowerReadStrength = nodeTracker.get_average_strength_connected()
    intWorkingRange = intWorkingRange/2
    
    return (nodeTracker, intWorkingRange, strDirection, \
            intLowerReadPosition, intHigherReadPosition, boolLower)





def Search1(nodeTracker, strDirection):

    intHigherReadStrength = 0
    intHigherReadPosition = 180
    intLowerReadStrenth = 0
    intLowerReadPosition = 0
    intWorkingRange = intHigherReadPosition - intLowerReadPosition
    boolLooking = True
    
    #get signal strengths from current max and min degrees
    nodeTracker.move(strDirection, intLowerReadPosition) #not implimented yet
    intLowerReadStrength = nodeTracker.get_average_strength_connected()
    nodeTracker.move(strDirection, intHigherReadPosition) #not implimented yet
    intHigherReadStrength = nodeTracker.get_average_strength_connected()
    boolLower = False
    intWorkingRange = intWorkingRange/2
    while(boolLooking):
        
        if (intWorkingRange<2):
            boolLooking = False
            break
        step = Search_Step(nodeTracker, intWorkingRange, strDirection, \
                intLowerReadPosition, intLowerReadStrenght,\
                intHigherReadPosition, intHigherReadStrength,\
                boolLower)

        nodeTracker = step[0]
        intWorkingRange = step[1]
        intLowerReadPosition = step[3]
        intHigherReadPosition = step[4]
        boolLower = step[5]


    #return the half-way point of the final angles
    intFinalDegree = int(((intHigherReadPosition-intLowerReadPosition)/2+ \
            intLowerReadPosition))
    nodeTracker.move(strDirection, intFinalDegree)
    intFinalStrength = nodeTracker.get_average_strength_connected()

    if (strDirection == "pan"):
        nodeTracker.intServoPanDegree = intFinalDegree
    elif (strDirection == "tilt"):
        nodeTracker.intServoTiltDegree = intFinalDegree
    nodeTracker.intWifiStrength = intFinalStrength

    return (nodeTracker)

