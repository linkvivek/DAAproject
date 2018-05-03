
#This class is associated with each vertex instance and methods

import sys
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxint                      # Set distance to infinity for all nodes
        self.visited = False                            # Mark all nodes unvisited
        self.previous = None                            # Predecessor

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def set_not_visited(self):
        self.visited = False

    def reset_distance(self):
        self.distance = sys.maxint

    # def get_id(self):
    #     return self.id

        # def __str__(self):
    #     return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

