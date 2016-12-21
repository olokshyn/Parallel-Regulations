from GraphRepr import (AdjacencyList as Al,
                       ALVertex as Vx,
                       AdjacencyMatrix as Am,
                       EdgesList as El)


def al_acyclic_graph_1():
    return Al([
        Vx(0, (1, 2)),
        Vx(1, (4, 5)),
        Vx(2, (6, 7)),
        Vx(3, 7),
        Vx(4),
        Vx(5, 8),
        Vx(6, 8),
        Vx(7),
        Vx(8)
    ])


def am_acyclic_graph_1():
    return Am([
        [0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])


def el_acyclic_graph_1():
    return El([
        [0, 1],
        [0, 2],
        [1, 4],
        [1, 5],
        [2, 6],
        [2, 7],
        [3, 7],
        [5, 8],
        [6, 8]
    ])


def al_acyclic_graph_2():
    return Al([
        Vx(0, (1, 2)),
        Vx(1, (4, 5)),
        Vx(2, (6, 7, 9)),
        Vx(3, 7),
        Vx(4),
        Vx(5, 8),
        Vx(6, 8),
        Vx(7, 9),
        Vx(8, 9),
        Vx(9),
        Vx(10, 2)
    ])


def al_acyclic_graph_3():
    return Al([
        Vx(0, (2, 3)),
        Vx(1, 2),
        Vx(2, (3, 4)),
        Vx(3, (5, 6)),
        Vx(4, 7),
        Vx(5, 7),
        Vx(6),
        Vx(7)
    ])


def al_acyclic_graph_4():
    return Al([
        Vx(0, (1, 2, 5)),
        Vx(1, (3, 4, 5)),
        Vx(2, 6),
        Vx(3, 7),
        Vx(4, 7),
        Vx(5, 8),
        Vx(6, 8),
        Vx(7, 9),
        Vx(8, 9),
        Vx(9),
        Vx(10, 12),
        Vx(11, 12),
        Vx(12, (6, 13)),
        Vx(13)
    ])


def al_acyclic_graph_5():
    return Al([
        Vx(0, 4),
        Vx(1, 5),
        Vx(2, (6, 7)),
        Vx(3, 7),
        Vx(4, 11),
        Vx(5, 11),
        Vx(6, 11),
        Vx(7, 8),
        Vx(8, (9, 10)),
        Vx(9),
        Vx(10),
        Vx(11, (12, 13, 14)),
        Vx(12),
        Vx(13),
        Vx(14)
    ])


def al_cyclic_graph_1():
    return Al([
        Vx(0, (2, 3)),
        Vx(1, 2),
        Vx(2, (3, 4)),
        Vx(3, (5, 6)),
        Vx(4, 7),
        Vx(5, 7),
        Vx(6, 8),
        Vx(7),
        Vx(8, 2)
    ])


def al_cyclic_graph_2():
    return Al([
        Vx(0, (1, 2, 3)),
        Vx(1, 4),
        Vx(2, 4),
        Vx(3, 2),
        Vx(4, 3)
    ])
