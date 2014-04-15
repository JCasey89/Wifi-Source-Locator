#! /usr/bin/env python3

import node
import search
import client

#strInterface = input("Please enter the name of the wireless interface: ")
strInterface = "wlp1s0"
tracker_1 = node.Node(strInterface)
tracker_2 = node.Node(strInterface)
#mode = input("Please enter 1 if you are connected to the target AP, otherwise\n\
#        enter 0 if you are not connected to the target AP: ")
mode = 1
if (int(mode) == 1):
#    intHope = search.Search1(tracker, "pan")
#    intPray = tracker.get_strength_connected()
#    print("%d db at %d degrees" % (intPray, intHope))
    
    connected = True

    print("tracker_1 pre search")
    print(tracker_1)
    searchTest1 = search.Search1(tracker_1, "pan", connected)
    print("tracker_1 post pan search")
    print(tracker_1)
    print("searchTest1 post pan search")
    print(searchTest1)
   # searchTest1 = search.Search1(tracker_1, "tilt", connected)
   # print("tracker_1 post tilt search")
   # print(tracker_1)
   # print("searchTest1 post tilt search")
   # print(searchTest1)
   # print("\n\n")

   # print("tracker_2 pre search")
   # print(tracker_2)
   # searchTest2 = search.Search2(tracker_2, connected)
   # print("tracker_2 post search")
   # print(tracker_2)
   # print("searchTest2 post search")
   # print(searchTest2)
else:
    target = tracker.select_target()

    
