
import node

def binarySearch(nodeTracker, strDirection):
    intHigherReadPosition = 180
    intLowerReadPosition = 0
    intWorkingRange = intHigherReadPosition - intLowerReadPosition
    boolLooking = True
    
#    assert type(strDirection) is StringType,\
#            "strDirection needs to be string type, current val is: %r"\
#            % strDirection
    

    #get signal strengths from current max and min degrees
    nodeTracker.move(strDirection, intLowerReadPosition) #not implimented yet
    intLowerReadStrength = nodeTracker.get_average_strength_connected()
    nodeTracker.move(strDirection, intHigherReadPosition) #not implimented yet
    intHigherReadStrength = nodeTracker.get_average_strength_connected()
    boolLeft = False
    intWorkingRange = intWorkingRange/2
    while(boolLooking):
        
        if (intWorkingRange<2):
            boolLooking = False
            break

        #binary search based off signal strengths
        if (intLowerReadStrength > intHigherReadStrength):
            intHigherReadPosition = int(intHigherReadPosition - intWorkingRange)
            boolLeft = True
            print("->")

        elif (intHigherReadStrength > intLowerReadStrength):
            intLowerReadPosition = int(intLowerReadPosition + intWorkingRange)
            print("<-")
            boolLeft = False
        elif (boolLeft):
            intWorkingRange =- 1
            intLowerReadPosition = intLowerReadPosition - 2
            nodeTracker.move(strDirection, intLowerReadPosition)
            intLowerReadStrength = nodeTracker.get_average_strength_connected()
            continue
        elif (not(boolLeft)):
            intWorkingRange =- 1
            intHigherReadPosition = intHigherReadPosition - 2
            nodeTracker.move(strDirection, intHigherReadPosition)
            intHigherReadStrength = nodeTracker.get_average_strength_connected()
            continue
        else:
            print("Something bad happened during the search")
            return -1
        if (boolLeft):
            nodeTracker.move(strDirection, intHigherReadPosition)
            intHigherReadStrength = nodeTracker.get_average_strength_connected()
        else:
            nodeTracker.move(strDirection, intLowerReadPosition)
            intLowerReadStrength = nodeTracker.get_average_strength_connected()
        intWorkingRange = intWorkingRange/2

    #return the half-way point of the final angles
    intFinalDegree = int(((intHigherReadPosition-intLowerReadPosition)/2+ \
            intLowerReadPosition))
    return intFinalDegree
