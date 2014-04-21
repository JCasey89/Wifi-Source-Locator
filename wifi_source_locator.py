#! /usr/bin/env python3

import node
import search
import client
import time

#strInterface = input("Please enter the name of the wireless interface: ")
strInterface = str(input("interface name: "))
tracker_1 = node.Node(strInterface)
#tracker_2 = node.Node(strInterface)

host_ip = input("Please enter server IP address: ")
host_port = int(input("Please enter server port number: "))

answer = input("Are you connected to your target (y/n)? ")
if (answer.lower() == "y"):
    com_1 = client.socks()
#    com_2 = client.socks()
    
    connected = True

#    print("Searching Horizontal then Vertical")
    
    time1a = int(time.time())
    search.Search1(tracker_1, "pan", connected)
#    search.Search1(tracker_1, "tilt", connected)
    time1b = int(time.time())
   
#    print("\nAlternating search\n")

 #   time2a = int(time.time())
 #   search.Search2(tracker_2, connected)
 #   time2b = int(time.time())
    

    tracker_1.get_long_lat()
    tracker_1_data = str(tracker_1)
#    tracker_2_data = str(tracker_2)
    com_1.sendNodeData(host_ip, host_port, tracker_1_data.encode())
#    com_2.sendNodeData(host_ip, host_port, tracker_2_data.encode())
    print("time: %d" %(time1b - time1a))
#    print("Alt Horz and vert: %d" %(time2b - time2a))
else:
    done = False
    while not done:    
        com_1 = client.socks()
#        com_2 = client.socks()
        

        connected = False
        tracker_1.select_target()
#        tracker_2.strTargetBSSID = tracker_1.strTargetBSSID
    
#        print("Searching Horizontal then Vertical")
        
        time1a = int(time.time())
        search.Search1(tracker_1, "pan", connected)
#        search.Search1(tracker_1, "tilt", connected)
        time1b = int(time.time())
        
#        print("\nAlternating search\n")
#
#        time2a = int(time.time())
#        search.Search2(tracker_2, connected)
#        time2b = int(time.time())
        tracker_1.get_long_lat() 
        tracker_1_data = str(tracker_1)
#        tracker_2_data = str(tracker_2)
        com_1.sendNodeData(host_ip, host_port, tracker_1_data.encode())
#        com_2.sendNodeData(host_ip, host_port, tracker_2_data.encode())
        print("time: %d" %(time1b - time1a))
#        print("Alt Horz and vert: %d" %(time2b - time2a))
        cont = input("Are you done searching (y/n)? ")
        if cont.lower() == "y":
            done = True
            break
