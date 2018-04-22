
class Emergency:


    def __init__(self):
        import numpy as np
        import random
        import pandas as pd
        from pprint import pprint

        self.emergencyVehicles = pd.read_csv('EmergencyVehicles.csv')           #as pandas
        self.emergencyVehiclesSorted = sorted(set(self.emergencyVehicles['ZipCode']))
        # self.emergencyVehiclesSorted1 = self.emergencyVehicles['ZipCode'].unique()

        self.distance = pd.read_csv('distance.csv')           #as pandas
        self.request = pd.read_csv('request.csv')           #as pandas

        # emergencyVehiclesGrouped = emergencyVehicles.groupby(['ZipCode','Type'])['Type'].count()
        # emergencyVehiclesGrouped = emergencyVehicles.groupby(['ZipCode','Type'],as_index = False).apply(list)
        # emergencyVehiclesGrouped = emergencyVehicles.groupby(['ZipCode', 'Type'])
        # emergencyVehicles1 = emergencyVehiclesGrouped.index.get_level_values('ZipCode')


        # pprint(emergencyVehiclesGrouped)
        # aa = emergencyVehicles.loc[emergencyVehicles['ZipCode'] == 64151]
        # pprint(aa.loc[aa['Type'] == 1])

        # emergencyVehicles1 = emergencyVehicles.values       #pandas to array
        # pprint(emergencyVehicles1)
        # pprint(emergencyVehicles1[0][2])
        # pprint(self.emergencyVehiclesSorted)
        # pprint(self.emergencyVehiclesSorted1)
        # for k, v in emergencyVehiclesGrouped[64151][0]:
        #     print k
        #     print v
        #     print '===='



    def checkAvailability(self, zipCode, type):
        print zipCode
        zipCodeIndex = self.emergencyVehiclesSorted.index(zipCode)

        for i in range(len(self.emergencyVehiclesSorted)):
            # print self.emergencyVehicles[zipCodeIndex]
            aa = self.emergencyVehicles.loc[self.emergencyVehicles['ZipCode'] == zipCode]
            if(len((self.emergencyVehicles.loc[self.emergencyVehicles['ZipCode'] == zipCode]).loc[aa['Type'] == type]) > 0):
                bb = aa.loc[aa['Type'] == type]
                print zipCode
            #     print len(bb)


emergency = Emergency()

print emergency