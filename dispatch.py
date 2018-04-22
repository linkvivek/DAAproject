
def main():
    from pprint import pprint
    from Emergency import Emergency
    emergency = Emergency()

    # pprint(emergency.request['ID'])

    print len(emergency.request)
    for i in range(len(emergency.request)):
        print 'hi'
        pprint(emergency.request['ZipCode'][i])
        # pprint(emergency.request['VehicleType'][i])
        # print emergency.checkAvailability(1)

        emergency.checkAvailability(emergency.request['ZipCode'][i], emergency.request['VehicleType'][i])



main()