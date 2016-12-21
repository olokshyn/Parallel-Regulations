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

    def build_regulation(self, target_l, target_h):
        if not self.s_upper:
            self.build_s_upper()

        if len(self.s_upper) > target_l:
            raise RuntimeError('Cannot build regulation shorter than S-upper')

        regulation = deepcopy(self.s_upper)
        graph = deepcopy(self.graph)

        for i in xrange(target_l - len(regulation)):
            regulation.insert(0, set())

        k = 0
        while True:
            if len(regulation[k]) > target_h:
                return None
            if k + 1 == target_l:
                return regulation

            vertices_to_move_count = target_h - len(regulation[k])
            for i in xrange(k + 1, target_l):
                if not vertices_to_move_count:
                    break
                for vertex in graph.top_vertices & regulation[i]:
                    if not vertices_to_move_count:
                        break
                    regulation[i].remove(vertex)
                    regulation[k].add(vertex)
                    del graph.vertices[vertex]
                    vertices_to_move_count -= 1

            graph.find_top_vertices()

            k += 1

    def minimize_h(self, target_l):
        if not self.s_lower:
            self.build_s_lower()
        if not self.s_upper:
            self.build_s_upper()

        def get_regulation_height(regulation):
            return max(map(lambda x: len(x), regulation))

        h_min = len(self.graph.vertices) / target_l
        if len(self.graph.vertices) % target_l:
            h_min += 1
        h_max = min(get_regulation_height(self.s_lower),
                    get_regulation_height(self.s_upper))

        a = h_min
        b = h_max
        result_h = None
        result_regulation = None
        while a <= b:
            h = (a + b) / 2
            result_regulation = self.build_regulation(target_l, h)
            if result_regulation is not None:
                b = h - 1
                result_h = h
            else:
                a = h + 1
        return result_h, result_regulation
