
import subprocess
import re

# regex for 1 or more digit
number_pattern = re.compile("[0-9]+")
#
bssid_pattern = re.compile("[0-9a-f]+\:[0-9a-f]+\:[0-9a-f]+\:[0-9a-f]+\:[0-9a-f]+\:[0-9a-f]+")
signal_strength_pattern = re.compile("\-[0-9]+")



#Poll signal strength when connected to AP
# returns -db stripped of all non-digit symbols
def get_strength_connected(strInterface):
# read the relevant line of /proc/net/wireless for wireless strength
    file_read_process = subprocess.Popen("cat /proc/net/wireless | grep -i %r" %strInterface,\
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    file_line = file_read_process.stdout.readline()

    file_line = file_line.split()
# pull out the digits from the signal level value
    signal_strength = number_pattern.search(str(file_line[3]))
    sig_str = signal_strength.group()
#    print(sig_str)
    return int(sig_str)
