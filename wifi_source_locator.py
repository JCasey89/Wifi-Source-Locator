#! /usr/bin/env python3

import node
import search

strInterface = input("Please enter the name of the wireless interface: ")

tracker = node.Node(strInterface)

mode = input("Please enter 1 if you are connected to the target AP, otherwise\n\
        enter 0 if you are not connected to the target AP: ")
if (int(mode) == 1):
#    intHope = search.Search1(tracker, "pan")
#    intPray = tracker.get_strength_connected()
#    print("%d db at %d degrees" % (intPray, intHope))

    intHope = search.Search2(tracker)
    print(tracker)
else:
    tracker.select_target()
    
