
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





    def checkAvailability(self, zipCode = 64157, type = 2):
            # print zipCode

        zipCodeIndex = self.emergencyVehiclesSorted.index(zipCode)

        traverseLeftIndex = zipCodeIndex - 1
        traverseRightIndex = zipCodeIndex + 1

        distanceLeft = 0
        distanceRight = 0

        foundAtLeft = False
        foundAtRight = False


        for i in range(len(self.emergencyVehiclesSorted)):
            # print self.emergencyVehicles[zipCodeIndex]

            a = [10]
            b = [i+1]
            a.append(zipCode)
            a.append(type)

            traverseLeftZip = self.emergencyVehiclesSorted[traverseLeftIndex]
            traverseRightZip = self.emergencyVehiclesSorted[traverseRightIndex]

            # print traverseLeftZip
            # print traverseRightZip


            #traverse on the left direction
            ZipCodeRowsLeft = self.emergencyVehicles.loc[self.emergencyVehicles['ZipCode'] == traverseLeftZip]  #get the zip code rows from emergencyVehicles
            ZipCodeRowsRight = self.emergencyVehicles.loc[self.emergencyVehicles['ZipCode'] == traverseRightZip]  # get the zip code rows from emergencyVehicles

            if(foundAtLeft == False):
                distanceLeft = self.distance.loc[self.distance['ZipCode1'] == traverseLeftZip]['Distance'].values[0] + distanceLeft   # if available then get the distance
                traverseLeftIndex = traverseLeftIndex - 1

            if(foundAtRight == False):
                distanceRight = self.distance.loc[self.distance['ZipCode2'] == traverseRightZip]['Distance'].values[0] + distanceRight  # if available then get the distance
                traverseRightIndex = traverseRightIndex + 1

            if(len(ZipCodeRowsLeft.loc[ZipCodeRowsLeft['Type'] == type]) > 0):                #check if the requested vehicle is available
                a.append(ZipCodeRowsLeft['ID'].values[0])
                foundAtLeft = True

            # traverse on the right direction
            if (len(ZipCodeRowsRight.loc[ZipCodeRowsRight['Type'] == type]) > 0):  # check if the requested vehicle is available
                a.append(ZipCodeRowsLeft['ID'].values[0])
                foundAtRight = True

            # if(distanceLeft.values[0] != 0 and distanceRight.values[0] != 0):
            if(foundAtLeft and foundAtRight):
                distanceTotal =  self.compareDistance(distanceLeft, distanceRight)
                a.append(distanceTotal)
                b.append(a)
                # print a
                return b
                break



    def compareDistance(self, distanceLeft, distanceRight):

        if(distanceLeft < distanceRight):
            return distanceLeft
        elif(distanceLeft == distanceRight):
            return distanceLeft
        else: return distanceRight


    def another(self, currentZip = 64153, type = 2):
        import heapq

        # print unvisited_queue
        # heapq.heappush(unvisited_queue, (14, 64154))

        # print unvisited_queue
        # print heapq.heappop(unvisited_queue)


        # dd1 = self.distance.loc[(self.distance['ZipCode1'] == currentZip) | (self.distance['ZipCode2'] == currentZip)]  # if available then get the
        # print dd1['Distance']

        unvisited_queue = [(float("inf"), v) for v in self.emergencyVehiclesSorted]
        heapq.heapify(unvisited_queue)
        firstIteration = True

        while(unvisited_queue):
            dd1 = self.distance.loc[(self.distance['ZipCode1'] == currentZip) | (self.distance['ZipCode2'] == currentZip)]  # if available then get the
            for index, row in dd1.iterrows():
                # print row['ZipCode2']
                getVehicles = self.emergencyVehicles.loc[self.emergencyVehicles['ZipCode'] == row['ZipCode2']]  # get the zip code rows from emergencyVehicles
                # print getVihecles
                for k, v in getVehicles.iterrows():
                    if(type == v['Type']):
                        heapq.heappush(unvisited_queue, (row['Distance'], row['ZipCode2']))
                        print unvisited_queue
                    else:
                        currentZip = row['ZipCode2']






    def again(self, currentZip = 64153, type = 2):
        import heapq
        import sys

        edges = {}
        ss = {}

        unvisited_queue = [(v, None) for v in self.emergencyVehiclesSorted]
        heapq.heapify(unvisited_queue)

        distanceList = self.distance.values.tolist()
        # print aa[0][0]

        for each in distanceList:
            edges.setdefault(each[0], [])
            edges[each[0]].append(each[1])

        for index, row in self.distance.iterrows():
            # edges[row['ZipCode1']].append(ss)
            # edges[row['ZipCode1']][index] = {row['ZipCode2']:{'Distance':row['Distance']}}
            edges[row['ZipCode1']] += {row['ZipCode2']:{'Distance':row['Distance']}}

            # print row['ZipCode1']

        # print edges[64153]
        #
        # print edges
        # while not heapq.isEmpty():
        # for k, v in edges:
        #
        #         print v

        # print unvisited_queue

emergency = Emergency()

print emergency.another()