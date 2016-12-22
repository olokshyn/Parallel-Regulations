import sys

from Graph import Graph
from Regulation import Regulation
from BranchAndBound import BranchAndBound
from GraphRepr import GraphReprReader


def print_regulations(graph, target_l):
    r = Regulation(graph)
    h, regulation = r.minimize_h(target_l)

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


def print_branch_and_bound(graph, target_h):
    bb = BranchAndBound(target_h, graph)
    solutions = bb.solve()
    print 'Solutions with h = {0}:'.format(target_h)
    for solution in solutions:
        for row in solution:
            print ' '.join([str(x) for x in row])
        print ''


def load_graph():
    filename = raw_input('Enter the path to the graph file: ')
    return Graph(GraphReprReader.read_from_file(filename))


def enter_graph():
    return GraphReprReader.read_from_opened_file('al', sys.stdin)


def main():
    try:
        mode = raw_input('Chose mode:\n'
                         'load - load graph from file\n'
                         'read - read graph from input\n')
        if mode == 'load':
            graph = load_graph()
        elif mode == 'read':
            graph = enter_graph()
        else:
            raise ValueError('Unknown mode')

        mode = raw_input('Chose mode:\n'
                         'h - minimize h\n'
                         'l - minimize l\n')
        if mode == 'h':
            target_l = int(raw_input('Enter target l: '))
            print_regulations(graph, target_l)
        elif mode == 'l':
            target_h = int(raw_input('Enter target h: '))
            print_branch_and_bound(graph, target_h)

        return 0
    except Exception as exc:
        print exc.message
        return 1

if __name__ == '__main__':
    sys.exit(main())

