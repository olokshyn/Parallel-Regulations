from copy import deepcopy

from Graph import Graph


class Regulation(object):

    def __init__(self, graph):
        self.graph = graph
        self.s_lower = None
        self.s_upper = None

        assert isinstance(self.graph, Graph), \
            'graph object must be of type Graph'

    def build_s_lower(self):
        s = []
        temp_graph = deepcopy(self.graph)
        while temp_graph.top_vertices:
            s.append(temp_graph.top_vertices)
            for vertex in temp_graph.top_vertices:
                del temp_graph.vertices[vertex]
            temp_graph.find_top_vertices()
        self.s_lower = s
        return s

    def build_s_upper(self):
        s = []
        temp_graph = deepcopy(self.graph)
        while temp_graph.bottom_vertices:
            s.append(temp_graph.bottom_vertices)
            for vertex in temp_graph.vertices:
                temp_graph.vertices[vertex] -= \
                    temp_graph.bottom_vertices
            for vertex in temp_graph.bottom_vertices:
                del temp_graph.vertices[vertex]
            temp_graph.find_bottom_vertices()
        s.reverse()
        self.s_upper = s
        return s
