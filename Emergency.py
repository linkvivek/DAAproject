
class Emergency:
    from pprint import pprint

    def __init__(self):
        import numpy as np
        import random
        import pandas as pd
        from pprint import pprint

        self.emergencyVehicles = pd.read_csv('EmergencyVehicles.csv')           #as pandas
        self.emergencyVehiclesSorted = sorted(set(self.emergencyVehicles['ZipCode']))

        self.distance = pd.read_csv('distance.csv')           #as pandas
        self.request = pd.read_csv('request.csv')           #as pandas

        # d = self.distance.loc[self.distance['ZipCode1'] == 64155]
        # pprint(d)
        # print(d['Distance'])

        # print self.distance.loc[self.distance['ZipCode1'] == 64155]['Distance']




    def checkAvailability(self, zipCode = 64156, type = 1):

        zipCodeIndex = self.emergencyVehiclesSorted.index(zipCode)

        traverseLeftIndex = zipCodeIndex - 1
        traverseRightIndex = zipCodeIndex + 1

        traverseLeftZip = self.emergencyVehiclesSorted[traverseLeftIndex]
        traverseRightZip = self.emergencyVehiclesSorted[traverseRightIndex]

        distanceLeft = 0
        distanceRight = 0


        for i in range(len(self.emergencyVehiclesSorted)):
            # print self.emergencyVehicles[zipCodeIndex]

            #traverse on the left direction
            aa = self.emergencyVehicles.loc[self.emergencyVehicles['ZipCode'] == traverseLeftZip]  #get the zip code rows from emergencyVehicles
            # print(aa)
            if(len(aa) > 0 and len(aa.loc[aa['Type'] == type]) > 0):                                            #check if the requested vehicle is available
                distanceLeft = self.distance.loc[self.distance['ZipCode1'] == traverseLeftZip]['Distance'] + distanceLeft    # if available then get the distance
            else:
                traverseLeftIndex = traverseLeftIndex - 1


            # traverse on the right direction
            bb = self.emergencyVehicles.loc[self.emergencyVehicles['ZipCode'] == traverseRightZip]  # get the zip code rows from emergencyVehicles
            if (len(bb) > 0 and len(bb.loc[bb['Type'] == type]) > 0):  # check if the requested vehicle is available
                distanceRight = self.distance.loc[self.distance['ZipCode2'] == traverseRightZip]['Distance'] + distanceRight  # if available then get the distance
            else:
                traverseRightIndex = traverseRightIndex + 1

            print distanceLeft
            print distanceRight


emergency = Emergency()

print emergency