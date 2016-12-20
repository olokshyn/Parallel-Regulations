from GraphReprBase import GraphReprBase


class EdgesList(GraphReprBase):

    def __init__(self, edges_list):
        self.edges_list = edges_list

        for edge in edges_list:
            if len(edge) != 2:
                raise ValueError('Edges list must contain only'
                                 ' pairs of vertices numbers')

    def __iter__(self):
        return iter(self.edges_list)
