#!/usr/bin/env python

import subprocess
import re

# regex for 1 or more digit
number_pattern = re.compile("[0-9]+")

while True:
# read the relevant line of /proc/net/wireless for wireless strength *
    file_read_process = subprocess.Popen("cat /proc/net/wireless | grep -i wlp1s0",\
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    file_line = file_read_process.stdout.readline()

    file_line = file_line.split()
# pull out the digits from the signal level value (remove the - and the .)
    signal_strength = number_pattern.search(str(file_line[3]))
    print(signal_strength.group())
