from Vertex import Vertex


class Graph(object):

    def __init__(self, vertices_list):
        self.vertices = {}
        self.top_vertices = None

        for vertex in vertices_list:
            assert isinstance(vertex, Vertex), \
                'Graph can only be constructed from a list of Vertex objects'
            if vertex.index in self.vertices:
                raise ValueError('Vertex {0} specified more, than once'.format(vertex.index))
            self.vertices[vertex.index] = vertex.related_vertices

        for vertex in self.vertices:
            for related_vertex in self.vertices[vertex]:
                if related_vertex not in self.vertices:
                    raise ValueError('Invalid Graph: vertex {0} connected '
                                     'to not-specified vertex {1}'.format(vertex, related_vertex))

        self.find_top_vertices()
        if not self.top_vertices:
            raise ValueError('Invalid graph - there are no top vertices')

    def find_top_vertices(self):
        self.top_vertices = set(self.vertices.keys())
        for vertex in self.vertices:
            self.top_vertices -= set(self.vertices[vertex])

    def is_cyclic(self):

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
            for related_vertex in self.vertices[vertex]:
                if related_vertex in marked_vertices:
                    return True
                with MarkedVerticesGuard(marked_vertices, related_vertex):
                    if _is_cyclic(related_vertex, marked_vertices):
                        return True
            return False

        marked_vertices = set()
        for vertex in self.top_vertices:
            marked_vertices.add(vertex)
            if _is_cyclic(vertex, marked_vertices):
                return True
        return False

