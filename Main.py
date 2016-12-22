import sys

from Graph import Graph
from Regulation import Regulation
from GraphRepr import GraphReprReader


def print_results(r):
    target_l = raw_input('Enter desired l: ')
    h, regulation = r.minimize_h(int(target_l))

    print 'S-lower:'
    for row in r.s_lower:
        print ' '.join([str(x) for x in row])
    print ''

    print 'S-upper:'
    for row in r.s_upper:
        print ' '.join([str(x) for x in row])
    print ''

    print 'Minimal h: ', h
    print 'Regulation:'
    for row in regulation:
        print ' '.join([str(x) for x in row])


def load_graph():
    filename = raw_input('Enter the path to the graph file: ')
    print_results(Regulation(Graph(
        GraphReprReader.read_from_file(filename))))


def enter_graph():
    print_results(Regulation(Graph(
        GraphReprReader.read_from_opened_file('al', sys.stdin))))


def main():
    try:
        mode = raw_input('Chose mode:\n'
                         'load - load graph from file\n'
                         'read - read graph from input\n')
        if mode == 'load':
            load_graph()
        elif mode == 'read':
            enter_graph()
        else:
            raise ValueError('Unknown mode')
        return 0
    except Exception as exc:
        print exc.message
        return 1

if __name__ == '__main__':
    sys.exit(main())

