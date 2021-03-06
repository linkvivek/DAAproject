
#This class is associated with creation of vertices and edges

import pandas as pd
from vertex import Vertex

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

        self.emergencyVehicles = pd.read_csv('EmergencyVehicles.csv')                   # as pandas
        self.emergencyVehiclesSorted = self.emergencyVehicles['ZipCode'].unique()       # get unique zipcodes for iteration

        self.distance = pd.read_csv('distance.csv')                                     # as pandas
        self.request = pd.read_csv('request.csv')                                       # as pandas

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):                                 # creates new vertex
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):                                    # returns vextex for indivisual zip code
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):                        # creates new edge
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def set_previous(self, current):
        self.previous = current

    # def get_vertices(self):
    #     return self.vert_dict.keys()


    # def get_previous(self, current):
    #     return self.previous

