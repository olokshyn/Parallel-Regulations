import sys

from Graph import Graph
from Regulation import Regulation
from GraphRepr import GraphReprReader


def main():
    try:
        filename = raw_input('Enter the path to the graph file: ')
        r = Regulation(Graph(GraphReprReader.read_from_file(filename)))
        target_l = raw_input('Enter desired l: ')
        h, regulation = r.minimize_h(int(target_l))
        print 'Minimal h: ', h
        print 'Regulation:'
        for row in regulation:
            print ' '.join([str(x) for x in row])
        return 0
    except Exception as exc:
        print exc.message
        return 1


if __name__ == '__main__':
    sys.exit(main())

