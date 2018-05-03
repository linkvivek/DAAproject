import heapq
import pandas as pd

def dijkstra(aGraph, start, type, k):

    for v in aGraph:                                                # reset initial distance to default and status as not
        v.set_not_visited()                                         # visited for each vertex while iterating
        v.reset_distance()

    start.set_distance(0)                                           # Set the distance for the start node to zero, this node poped up first for iteration

    unvisited_queue = [(v.get_distance(), v) for v in aGraph]       # built a priority queue so the vertex with minimum distance
    heapq.heapify(unvisited_queue)                                  # gets poped up first

    dispatchOptions = pd.DataFrame(columns=['ID', 'Type', 'zip', 'VehicleID', 'distance', 'requestBY'])      # pandas dataframe to store all the available vertices

    while len(unvisited_queue):

        uv = heapq.heappop(unvisited_queue)                         # Pops a vertex with the smallest distance
        current = uv[1]

        current.set_visited()

        for next in current.adjacent:                                           # for every neighbour of a vertex, calculate distance only if its
            if (next.visited):                                                  # not visited already. There's no point to calculate distance between start vertex and visited vertex again.
                continue

            new_dist = current.get_distance() + current.get_weight(next)        # calculate distance between current vertex and its neighbour
            next.set_distance(new_dist)
            # next.set_previous(current)

            #Extract the zipcodes which have the requested vehicle type from emergencyVehicles dataframe
            available = aGraph.emergencyVehicles.loc[(aGraph.emergencyVehicles['ZipCode'] == next.id) & (aGraph.emergencyVehicles['Type'] == type)]

            if (len(available) > 0):                                              # store all the possible zipcodes that have the requested vehicle types
                VehicleID = available['ID'].values
                dispatchOptions = dispatchOptions.append({"ID": [k], "Type": [type], "zip": [next.id], "VehicleID": [VehicleID[0]], "distance": new_dist, "requestBY": [start.id]}, ignore_index=True)

        # while len(unvisited_queue):
        #     heapq.heappop(unvisited_queue)

        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]  # Put all vertices not visited into the queue to get the next closer vertex
        heapq.heapify(unvisited_queue)


    if(len(dispatchOptions)):
        closestZipcode = dispatchOptions.loc[dispatchOptions['distance'].idxmin()]                                           # among all available options extract the one with minimum distance
        aGraph.emergencyVehicles = aGraph.emergencyVehicles[aGraph.emergencyVehicles.ID != closestZipcode['VehicleID']]      # remove the chosen id from dataframe so it wont get picked again
        return closestZipcode
    else:
        dispatchOptions = dispatchOptions.append({"ID": [k], "Type": [type], "zip": 0, "VehicleID": 0, "distance": 0, "requestBY": [start.id]},ignore_index=True)       # if requested vehicle is not available, return empty
        return dispatchOptions




