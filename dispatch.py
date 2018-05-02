from graph import Graph
from dijkstra import dijkstra

def dispatchVihecles():

    g = Graph()
    list = []
    for everyZip in g.emergencyVehiclesSorted:
        g.add_vertex(everyZip)


    for k, v in g.distance.iterrows():
        g.add_edge(v['ZipCode1'], v['ZipCode2'], v['Distance'])

    print 'Graph data:'
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            # print '( %s , %s, %3d)' % (vid, wid, v.get_weight(w))

    for k, v in g.request.iterrows():
        start = int(v['ZipCode'])
        type = int(v['VehicleType'])
        # print start
        # print type
        min = dijkstra(g, g.get_vertex(start), type)
        # list.append(min)

    print min
    target = g.get_vertex(64159)
    path = [target.get_id()]
    # shortest(target, path)
    # print 'The shortest path : %s' % (path[::-1])


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


dispatchVihecles()      #calling the main function

# http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php