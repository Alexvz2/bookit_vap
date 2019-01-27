# Purpose: This File containes the functions needed to generate and quantify the
#          access points connections to the physical routers
# Date: 27/01/19
# Author: Alex Vazquez
# bssid unqie to router
# DA is mac address 6  octects
# SA source adress

import subprocess
import re


# downloads and updates aircrack-ng
def First_Time():
    subprocess.call("sudo apt-get install aircrack-ng")  # downalod aircrack if hasnt been installed
    pass


# Purpose: Selects and initiliazes wifi adapter to scan the traffic
# input: device number to run monitor mode on
# output: Treu if worked, False if error
def Initialize(deviceNum):
    try:
        subprocess.call("sudo airmon-ng start wlan%d" % deviceNum)
    except Exception as e:
        print("ERROR... %s" % e)
        return
    return True


# Purpose: Open .txt file and write traffic to it in determined time span
# inputs:
#    deviceNum: device number to run monitor mode on
#    tim: time to execute command for
def Import_Traffic(deviceNum, tim):
    file_ = open("Traffic.txt", "w")
    subprocess.Popen([" timeout %i sudo tcpdump -i wlan%dmon -e" % (tim, deviceNum)], stdout=file_)
    pass


# Purpose: counts number of mac adresses
# input: size: size of max capacity of building
# output: number of unique mac adresses
def Mac_count(size):
    file_ = open("Traffic.txt", "r")
    dict = [0]*size
    count = 0

    for line in file_:
        address = re.findall(('(?:[0-9a-fA-F]{1,}(?:\-|\:)){5}[0-9a-fA-F]{1,}'), line)
        if not (dict.contains(address)):
            dict.add(address)
            count += 1
            pass
    return count


# Purpose: determines the vacancy of the building
# input:
#   size: size of max capacity of building
#   mac_num: unqiue mac adresses connected to AP
# output: Vacancy percentage (out of a 100)
def vacancy_det(size, mac_num):
    vacancy = 100 - (size/max(mac_num, 1) * 100)  # vacancy percentage
    return vacancy
