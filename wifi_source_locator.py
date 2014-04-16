#! /usr/bin/env python3

import node
import search
import client

#strInterface = input("Please enter the name of the wireless interface: ")
strInterface = "wlp1s0"
tracker_1 = node.Node(strInterface)
tracker_2 = node.Node(strInterface)
mode = input("Please enter 1 if you are connected to the target AP, otherwise\n\
        enter 0 if you are not connected to the target AP: ")
if (int(mode) == 1):
    
    connected = True

    search.Search1(tracker_1, "pan", connected)
    search.Search1(tracker_1, "tilt", connected)
    search.Search2(tracker_2, connected)
else:
    
    connected = False

    tracker_1.select_target()
#    search.Search1(tracker_1, "pan", connected)
#    search.Search1(tracker_1, "tilt", connected)
#    print(tracker_1)
    tracker_2.strTargetBSSID = tracker_1.strTargetBSSID
    search.Search2(tracker_2, connected)
    print(tracker_2)
