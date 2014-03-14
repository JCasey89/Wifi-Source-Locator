#! /usr/bin/env python

import node
import search

strInterface = input("Please enter the name of the wireless interface: ")

tracker = node.Node(strInterface)

print(tracker.strInterfaceName)
intHope = search.binarySearch(tracker, "pan")
intPray = tracker.get_strength_connected()
print("%d db at %d degrees" % (intPray, intHope))
