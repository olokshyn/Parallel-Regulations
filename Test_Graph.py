from unittest import TestCase

from Vertex import Vertex
from Graph import Graph


def create_acyclic_graph_1():
    return [Vertex(0, (1, 2)),
            Vertex(1, (4, 5)),
            Vertex(2, (6, 7)),
            Vertex(3, 7),
            Vertex(4),
            Vertex(5, 8),
            Vertex(6, 8),
            Vertex(7),
            Vertex(8)]


def create_acyclic_graph_2():
    return [Vertex(0, (1, 2)),
            Vertex(1, (4, 5)),
            Vertex(2, (6, 7, 9)),
            Vertex(3, 7),
            Vertex(4),
            Vertex(5, 8),
            Vertex(6, 8),
            Vertex(7, 9),
            Vertex(8, 9,),
            Vertex(9),
            Vertex(10, 2)]


def create_acyclic_graph_3():
    return [Vertex(0, (2, 3)),
            Vertex(1, 2),
            Vertex(2, (3, 4)),
            Vertex(3, (5, 6)),
            Vertex(4, 7),
            Vertex(5, 7),
            Vertex(6),
            Vertex(7)]


def create_cyclic_graph_1():
    return [Vertex(0, (2, 3)),
            Vertex(1, 2),
            Vertex(2, (3, 4)),
            Vertex(3, (5, 6)),
            Vertex(4, 7),
            Vertex(5, 7),
            Vertex(6, 8),
            Vertex(7),
            Vertex(8, 2)]


def create_cyclic_graph_2():
    return [Vertex(0, (1, 2, 3)),
            Vertex(1, 4),
            Vertex(2, 4),
            Vertex(3, 2),
            Vertex(4, 3)]


class TestGraph(TestCase):

    def test_init(self):
        Graph(create_acyclic_graph_1())

        Graph(create_acyclic_graph_2())

        Graph(create_acyclic_graph_3())

    def test_find_top_vertices(self):
        g = Graph(create_acyclic_graph_1())
        self.assertEqual({0, 3}, g.top_vertices)

        g = Graph(create_acyclic_graph_2())
        self.assertEqual({0, 3, 10}, g.top_vertices)

        g = Graph(create_acyclic_graph_3())
        self.assertEqual({0, 1}, g.top_vertices)

    def test_is_cyclic(self):
        g = Graph(create_acyclic_graph_1())
        self.assertFalse(g.is_cyclic())

        g = Graph(create_acyclic_graph_2())
        self.assertFalse(g.is_cyclic())

        g = Graph(create_acyclic_graph_3())
        self.assertFalse(g.is_cyclic())

        g = Graph(create_cyclic_graph_1())
        self.assertTrue(g.is_cyclic())

        g = Graph(create_cyclic_graph_2())
        self.assertTrue(g.is_cyclic())
