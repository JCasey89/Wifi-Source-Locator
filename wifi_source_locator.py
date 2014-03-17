#! /usr/bin/env python

import node
import search

strInterface = input("Please enter the name of the wireless interface: ")

tracker = node.Node(strInterface)

mode = input("Please enter 1 if you are connected to the target AP, otherwise\n\
        enter 0 if you are not connected to the target AP: ")
if (int(mode) == 1):
    intHope = search.binarySearch(tracker, "pan")
    intPray = tracker.get_strength_connected()
    print("%d db at %d degrees" % (intPray, intHope))
else:
    tracker.select_target()
