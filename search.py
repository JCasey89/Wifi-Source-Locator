
import node
import sys

def Search_Step(nodeTracker, intWorkingRange, strDirection, \
        intLowerReadPosition, intHigherReadPosition, boolLower):
    #binary search based off signal strengths
    if (intLowerReadStrength > intHigherReadStrength):
        intHigherReadPosition = int(intHigherReadPosition - intWorkingRange)
        boolLower = True
        print("->")

    elif (intHigherReadStrength > intLowerReadStrength):
        intLowerReadPosition = int(intLowerReadPosition + intWorkingRange)
        print("<-")
        boolLower = False
    elif (boolLower):
        intWorkingRange =- 1
        intLowerReadPosition = intLowerReadPosition - 2
        nodeTracker.Move(strDirection, intLowerReadPosition)
        intLowerReadStrength = nodeTracker.get_average_strength_connected()
        continue
    elif (not(boolLower)):
        intWorkingRange =- 1
        intHigherReadPosition = intHigherReadPosition - 2
        nodeTracker.Move(strDirection, intHigherReadPosition)
        intHigherReadStrength = nodeTracker.get_average_strength_connected()
        continue
    else:
        print("Something bad happened during the search")
        return -1
    if (boolLower):
        nodeTracker.Move(strDirection, intHigherReadPosition)
        intHigherReadStrength = nodeTracker.get_average_strength_connected()
    else:
        nodeTracker.Move(strDirection, intLowerReadPosition)
        intLowerReadStrength = nodeTracker.get_average_strength_connected()
    intWorkingRange = intWorkingRange/2
    
    return (nodeTracker, intWorkingRange, strDirection, \
            intLowerReadPosition, intHigherReadPosition, boolLower)





def Search(nodeTracker, strDirection):
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
    boolLower = False
    intWorkingRange = intWorkingRange/2
    while(boolLooking):
        
        if (intWorkingRange<2):
            boolLooking = False
            break
        step = Search_Step(nodeTracker, intWorkingRange, strDirection, \
                intLowerReadPosition, intHigherReadPosition, boolLower)

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
    return (intFinalDegree, intFinalStrneght)
