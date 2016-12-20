class Vertex(object):

    def __init__(self, vertex_index, related_vertices=tuple()):
        self.index = vertex_index
        if isinstance(related_vertices, tuple):
            self.related_vertices = related_vertices
        elif isinstance(related_vertices, list):
            self.related_vertices = tuple(related_vertices)
        elif isinstance(related_vertices, int):
            self.related_vertices = (related_vertices,)
        else:
            assert False, 'related_vertices has invalid type'
