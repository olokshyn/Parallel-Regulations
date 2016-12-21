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

    @staticmethod
    def read_from_file(input_file):
        edges_list = []
        for line in input_file:
            row = map(lambda x: int(x), line.split())
            if not row:
                raise ValueError('File contains empty row')
            edges_list.append(row)
        return EdgesList(edges_list)
