
class Emergency:


    def __init__(self):
        import numpy as np
        import random
        import pandas as pd
        from pprint import pprint

        emergencyVehicles = pd.read_csv('emergencyVehicles.csv')           #as pandas
        distance = pd.read_csv('distance.csv')           #as pandas
        request = pd.read_csv('request.csv')           #as pandas

        EmergencyVehicles = emergencyVehicles.groupby(['ZipCode','Type'])['Type'].count()

        pprint(EmergencyVehicles[64151][1])
        pprint(request)

    def checkAvailability(self):



emergency = Emergency()

print emergency