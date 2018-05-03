from graph import Graph
from dijkstra import dijkstra
import pandas as pd

def dispatchVihecles():

    g = Graph()
    result = pd.DataFrame(columns=['ID', 'Type', 'zip', 'VehicleID', 'distance'])       # dataframe to store final results in

    for everyZip in g.emergencyVehiclesSorted:                                          # adding each zipcodes as vetex
        g.add_vertex(everyZip)


    for k, v in g.distance.iterrows():                                                  # creating the edges
        g.add_edge(v['ZipCode1'], v['ZipCode2'], v['Distance'])

    for k, v in g.request.iterrows():                                                   # iterating over each request to get the minimum distance using dijkstra algorithm
        start = int(v['ZipCode'])
        type = int(v['VehicleType'])

        minimumDistanceRow = dijkstra(g, g.get_vertex(start), type, k+1)
        result = result.append(minimumDistanceRow)                                      # append the returned minimum distance row into a dataframe to display results

    print result


dispatchVihecles()      #calling the main function




# Reference:
# http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php