import os

from AdjacencyList import AdjacencyList
from AdjacencyMatrix import AdjacencyMatrix
from EdgesList import EdgesList


class GraphReprReader(object):

    @staticmethod
    def read_from_file(filename):
        if not os.path.exists(filename):
            raise ValueError('File {0} does not exist'.format(filename))
        file_format = os.path.basename(filename).split('.')[1]
        with open(filename, 'r') as input_file:
            if file_format == 'al':
                return AdjacencyList.read_from_file(input_file)
            elif file_format == 'am':
                return AdjacencyMatrix.read_from_file(input_file)
            elif file_format == 'el':
                return EdgesList.read_from_file(input_file)
            else:
                raise ValueError('Unknown file format')
        raise ValueError('Failed to read file')
