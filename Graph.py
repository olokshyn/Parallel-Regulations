from GraphRepr import (GraphReprBase,
                       AdjacencyList,
                       AdjacencyMatrix,
                       EdgesList)


class Graph(object):
    def __init__(self, vertices):
        self.vertices = {}
        self.top_vertices = None
        self.bottom_vertices = None

        assert isinstance(vertices, GraphReprBase), \
            'Graph can be constructed only from GraphRepr object'

        if isinstance(vertices, AdjacencyList):
            self._init_from_adjacency_list(vertices)
        elif isinstance(vertices, AdjacencyMatrix):
            self._init_from_adjacency_matrix(vertices)
        elif isinstance(vertices, EdgesList):
            self._init_from_edges_list(vertices)
        else:
            assert False, 'Unsupported graph representation type'

        for vertex in self.vertices:
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in self.vertices:
                    raise ValueError('Invalid Graph: vertex {0} connected '
                                     'to not-specified vertex {1}'.format(vertex, adjacent_vertex))

        self.find_top_vertices()
        self.find_bottom_vertices()

    def _init_from_adjacency_list(self, adjacency_list):
        for vertex in adjacency_list:
            if vertex.index in self.vertices:
                raise ValueError('Vertex {0} specified more, than once'.format(vertex.index))
            self.vertices[vertex.index] = set(vertex.adjacent_vertices)

    def _init_from_adjacency_matrix(self, adjacency_matrix):
        for i, adjacency_row in enumerate(adjacency_matrix):
            if i not in self.vertices:
                self.vertices[i] = set()
            for j, adjacency in enumerate(adjacency_row):
                if adjacency == 1:
                    if j in self.vertices[i]:
                        raise ValueError('Adjacency matrix contains bi-directional edge')
                    self.vertices[i].add(j)

    def _init_from_edges_list(self, edges_list):
        for edge in edges_list:
            if len(edge) != 2:
                raise ValueError('Invalid edge')
            if edge[0] not in self.vertices:
                self.vertices[edge[0]] = set()
            if edge[1] not in self.vertices:
                self.vertices[edge[1]] = set()
            self.vertices[edge[0]].add(edge[1])

    def __eq__(self, other):
        return self.vertices == other.vertices \
               and self.top_vertices == other.top_vertices

    def find_top_vertices(self):
        self.top_vertices = set(self.vertices)
        for vertex in self.vertices:
            self.top_vertices -= self.vertices[vertex]

    def find_bottom_vertices(self):
        self.bottom_vertices = set()
        for vertex in self.vertices:
            if not self.vertices[vertex]:
                self.bottom_vertices.add(vertex)

    def is_cyclic(self):
        if not self.top_vertices or not self.bottom_vertices:
            return True

        class MarkedVerticesGuard(object):

            def __init__(self, marked_vertices, vertex_to_add):
                assert isinstance(marked_vertices, set), \
                    "marked_vertices must be of type set"

                self.marked_vertices = marked_vertices
                self.vertex_to_add = vertex_to_add

            def __enter__(self):
                self.marked_vertices.add(self.vertex_to_add)

            def __exit__(self, exc_type, exc_val, exc_tb):
                self.marked_vertices.remove(self.vertex_to_add)

        def _is_cyclic(vertex, marked_vertices):
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex in marked_vertices:
                    return True
                with MarkedVerticesGuard(marked_vertices, adjacent_vertex):
                    if _is_cyclic(adjacent_vertex, marked_vertices):
                        return True
            return False

        marked_vertices = set()
        for vertex in self.top_vertices:
            marked_vertices.add(vertex)
            if _is_cyclic(vertex, marked_vertices):
                return True
        return False

    def send_stream(self, vertices):
        if vertices - self.top_vertices:
            raise ValueError('Cannot send stream starting from non-top vertices')
        if self.is_cyclic():
            raise ValueError('Cannot send stream through a cyclic graph')

        def _send_stream(vertex, marked_vertices):
            adjacent_vertices = self.vertices[vertex]
            if not adjacent_vertices:
                drain = 1
            else:
                drain = 0
                for adjacent_vertex in adjacent_vertices:
                    if adjacent_vertex not in marked_vertices:
                        marked_vertices.add(adjacent_vertex)
                        drain += _send_stream(adjacent_vertex,
                                              marked_vertices)
            return drain

        drain = 0
        marked_vertices = set()
        for vertex in vertices:
            marked_vertices.add(vertex)
            drain += _send_stream(vertex, marked_vertices)
        return drain
