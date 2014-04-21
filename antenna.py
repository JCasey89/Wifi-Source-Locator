#! /usr/bin/env python3
import subprocess
import re
import time

# regex for 1 or more digit
number_pattern = re.compile("[0-9]+")
#
bssid_pattern = re.compile("[0-9a-f]+\:[0-9a-f]+\:[0-9a-f]+\:[0-9a-f]+\:[0-9a-f]+\:[0-9a-f]+")
signal_strength_pattern = re.compile("\-[0-9]+")



#Poll signal strength when connected to AP
# returns -db stripped of all non-digit symbols
def get_strength_connected(strInterface):
    time.sleep(1)
# read the relevant line of /proc/net/wireless for wireless strength
    read_process = subprocess.Popen("cat /proc/net/wireless | grep -i %r" %strInterface,\
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process_line = read_process.stdout.readline()

    process_line = process_line.split()
# pull out the digits from the signal level value
    signal_strength = number_pattern.search(str(process_line[3]))
    sig_str = signal_strength.group()
#    print(sig_str)
    return int(sig_str)

#Poll signal strength of all APs in range
def get_mac_strength_not_connected(strInterface):
# read the relevant lines from iw dev <device> scan for wireless strength
    read_process = subprocess.Popen("iw dev %r scan | egrep -i \"%s|signal\""\
            %(strInterface,strInterface), shell=True, stdout=subprocess.PIPE,\
            stderr=subprocess.PIPE)
    process_lines = []

#    print(read_process)
    while True:
        line = read_process.stdout.readline()
        if (not(line)):
            break
        process_lines.append(line)

    #slice process_lines into 2 lists 1 for BSSID 1 for sigStr
    array_strBSSID = process_lines[::2]
    array_intSignalStrength = process_lines[1::2]
    
#    print(array_strBSSID)
#    print(array_intSignalStrength)

    #init temp vars to hold matched regexes
    strMatchedBSSID = ""
    intMatchedSignalStrength = 0
    
    #make sure the arrays are the same size
    if (len(array_intSignalStrength) != len(array_strBSSID)):
        print("BSSID array size != Signal Strength array size in antenna.get_str()")
        return [("error", 1000)]

    #init return list of tubples
    array_tuple_strBSSID_intSingalStrength = []
    for i in range(len(array_strBSSID)):
        
        #match BSSID pattern and convert to string
        strMatchedBSSID = bssid_pattern.search(str(array_strBSSID[i]))
        strMatchedBSSID = str(strMatchedBSSID.group())

        #match Sig str pattern and convert to int
        intMatchedSignalStrength = signal_strength_pattern.search(str(\
                array_intSignalStrength[i]))

        intMatchedSignalStrength = int(intMatchedSignalStrength.group())
        
        #populate return array of tuples
        array_tuple_strBSSID_intSingalStrength.append((strMatchedBSSID,\
                intMatchedSignalStrength))
    
    return array_tuple_strBSSID_intSingalStrength
