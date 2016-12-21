from GraphReprBase import GraphReprBase


class Vertex(object):

    def __init__(self, vertex_index, adjacent_vertices=None):
        self.index = vertex_index
        if adjacent_vertices is None:
            self.adjacent_vertices = set()
        elif isinstance(adjacent_vertices, tuple) \
                or isinstance(adjacent_vertices, list):
            self.adjacent_vertices = set(adjacent_vertices)
        elif isinstance(adjacent_vertices, int):
            self.adjacent_vertices = {adjacent_vertices}
        else:
            assert False, 'adjacent_vertices has invalid type'


class AdjacencyList(GraphReprBase):

    def __init__(self, adjacency_list):
        for v in adjacency_list:
            assert isinstance(v, Vertex), \
                "adjacency_list must consist of Vertex objects"
        self.adjacency_list = adjacency_list

    def __iter__(self):
        return iter(self.adjacency_list)

    @staticmethod
    def read_from_file(input_file):
        adjacency_list = []
        for line in input_file:
            row = map(lambda x: int(x), line.split())
            if not row:
                raise ValueError('File contains empty row')
            adjacency_list.append(Vertex(row[0], row[1:]))
        return AdjacencyList(adjacency_list)
