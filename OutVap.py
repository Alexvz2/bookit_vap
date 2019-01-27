# Purpose: Script to run every 30 mins, obtain traffic figures on the network and
#               submit to database
#
# Date: 27/01/19
import BookItVap as bkLib
from pymongo import MongoClient
import time
import datetime


client = MongoClient('mongodb://admin:admin1234@ds113815.mlab.com:13815/bookit’)
db = client.Bookit
collection = db.VAP


# Inputs:
#   t/f- True if first time running or updating pck, else false
#   deviceNum- device number to run monitor mode one
#   t- time span to execute and quanitify monitor mode output for
#   size- max capacity of building
#   location- name of location in building
def upload_traffic(t/f, deviceNum, t, size, location):
    if t/f:
        bkLib.First_Time()
        time.sleep(5)
        pass
    bkLib.Initialize(deviceNum, t)
    time.sleep(5)
    while err:
        try:
            bkLib.Import_Traffic(deviceNum, t)
            time.sleep(5)
            mac_num = bkLib.Mac_count(size)
            building_data = {
                "Building": "Life",
                "Location": location,
                "date": datetime.datetime.utcnow(),
                "Capacity": size,
                "Connections": mac_num,
                "Vacancy": bkLib.vacancy_det(size, mac_num)
                }
            result = collection.insert_one(building_data)
            time.sleep(1.8*10**6)  # repeat every 30 mins
        except Exception as err:
            raise
    pass


# Prevent from running function without directly running script
if __name__ == "__main__":
    upload_traffic(True, 1, 100, 100000, "Life building")
    return True
