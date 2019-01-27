# Purpose: This File containes the functions needed to generate and qunatify the
#          access points connections to the physical routers
# Date: 27/01/19
# Author: Alex Vazquez
# bssid unqie to router
# DA is mac address 6  octects
# SA source adress
# - c count after amount of seconds


import subprocess


def First_Time():
    subprocess.call("sudo apt-get install aircrack-ng")  # downalod aircrack if hasnt been installed
    pass


# Device name 1 for this raspberry pi
def Initialize(deviceNum):
    subprocess.call("sudo airmon-ng start wlan%d" % deviceNum)
    return True


def import_Traffic(deviceNum, tim):
    file_ = open("ouput.txt", "w")
    subprocess.Popen([" timeout %i sudo tcpdump -i wlan%dmon -e" % (tim, deviceNum)], stdout=file_)
    pass
