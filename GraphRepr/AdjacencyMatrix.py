from GraphReprBase import GraphReprBase


class AdjacencyMatrix(GraphReprBase):

    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix

        n = len(self.adjacency_matrix)
        for adjacency_row in self.adjacency_matrix:
            if n != len(adjacency_row):
                raise ValueError('Adjacency matrix must be quadratic')
            for x in adjacency_row:
                if x != 0 and x != 1:
                    raise ValueError('Adjacency matrix should contain only 0, 1')

    def __iter__(self):
        return iter(self.adjacency_matrix)

    @staticmethod
    def read_from_file(input_file):
        adjacency_matrix = []
        for line in input_file:
            row = map(lambda x: int(x), line.split())
            if not row:
                raise ValueError('File contains empty row')
            adjacency_matrix.append(row)
        return AdjacencyMatrix(adjacency_matrix)
