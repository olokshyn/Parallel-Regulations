import os

from AdjacencyList import AdjacencyList
from AdjacencyMatrix import AdjacencyMatrix
from EdgesList import EdgesList


class GraphReprReader(object):

    @staticmethod
    def read_from_opened_file(graph_type, input_file):
        if graph_type == 'al':
            return AdjacencyList.read_from_file(input_file)
        elif graph_type == 'am':
            return AdjacencyMatrix.read_from_file(input_file)
        elif graph_type == 'el':
            return EdgesList.read_from_file(input_file)
        else:
            raise ValueError('Unknown file format')

    @staticmethod
    def read_from_file(filename):
        if not os.path.exists(filename):
            raise ValueError('File {0} does not exist'.format(filename))
        file_format = os.path.basename(filename).split('.')[1]
        with open(filename, 'r') as input_file:
            return GraphReprReader.read_from_opened_file(file_format,
                                                         input_file)
