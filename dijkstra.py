import heapq
import sys
from graph import Graph
import pandas as pd
g = Graph()

def dijkstra(aGraph, start, type):
    # print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero
    start.set_distance(0)
    for v in aGraph:
        v.set_not_visited()

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    pathHeap = [(sys.maxint, sys.maxint, sys.maxint) for v in aGraph]
    heapq.heapify(pathHeap)
    min_list = []
    dff = pd.DataFrame()
    # df = pd.DataFrame({"distance": 0, "zip": 0, "ID": 0}, index=[0])
    df = pd.DataFrame(columns=['distance', 'zip', 'ID'])
    i = 1
    print '--------------------start -----------------'
    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            next.set_distance(new_dist)
            next.set_previous(current)
            z = g.emergencyVehicles.loc[(g.emergencyVehicles['ZipCode'] == next.id) & (g.emergencyVehicles['Type'] == type)]

            if (len(z)>0):
                idd = z['ID'].values
                for v in idd:
                    id = v
                df = df.append({"distance": int(new_dist), "zip": int(next.id), "ID": int(id)}, ignore_index=True)
                heapq.heappush(pathHeap, (new_dist, next.id, id))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

    if(len(df)):
        minrow = df.loc[df['distance'].idxmin()]
        dff = dff.append(minrow)
        # print minrow
        g.emergencyVehicles = g.emergencyVehicles[g.emergencyVehicles.ID != int(minrow['ID'])] #remove the id from dataframe

    return dff




