from graph import Graph

import heapq


def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)
    print unvisited_queue
    print '======'

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                      % (current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                      % (current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)



def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return



if __name__ == '__main__':

    g = Graph()
    # for k, v in g.emergencyVehiclesSorted:
    for i in g.emergencyVehiclesSorted:
        # print i
        g.add_vertex(i)


    for k, v in g.distance.iterrows():
        # print v['ZipCode1']
        g.add_edge(v['ZipCode1'], v['ZipCode2'], v['Distance'])

    print 'Graph data:'
    print g
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)' % (vid, wid, v.get_weight(w))

    dijkstra(g, g.get_vertex(64153), g.get_vertex(64159))

    target = g.get_vertex(64159)
    path = [target.get_id()]
    shortest(target, path)
    print 'The shortest path : %s' % (path[::-1])



# http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php