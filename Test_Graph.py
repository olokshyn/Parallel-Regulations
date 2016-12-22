from unittest import TestCase

from Graph import Graph
from GraphRepr import GraphReprReader
import CreateGraph


class TestGraph(TestCase):
    def test_init(self):
        g_al = Graph(CreateGraph.al_acyclic_graph_1())
        g_am = Graph(CreateGraph.am_acyclic_graph_1())
        g_el = Graph(CreateGraph.el_acyclic_graph_1())

        self.assertEqual(g_al, g_am)
        self.assertEqual(g_al, g_el)

        Graph(CreateGraph.al_acyclic_graph_2())

        Graph(CreateGraph.al_acyclic_graph_3())

    def test_load_from_file(self):
        g1 = Graph(CreateGraph.al_acyclic_graph_1())

        g1_al = Graph(GraphReprReader.read_from_file('TestFiles/Graph1.al'))
        g1_am = Graph(GraphReprReader.read_from_file('TestFiles/Graph1.am'))
        g1_el = Graph(GraphReprReader.read_from_file('TestFiles/Graph1.el'))

        self.assertEqual(g1, g1_al)
        self.assertEqual(g1, g1_am)
        self.assertEqual(g1, g1_el)

        g2 = Graph(CreateGraph.al_acyclic_graph_2())

        g2_al = Graph(GraphReprReader.read_from_file('TestFiles/Graph2.al'))

        self.assertEqual(g2, g2_al)

    def test_find_top_vertices(self):
        g = Graph(CreateGraph.al_acyclic_graph_1())
        self.assertEqual({0, 3}, g.top_vertices)

        g = Graph(CreateGraph.al_acyclic_graph_2())
        self.assertEqual({0, 3, 10}, g.top_vertices)

        g = Graph(CreateGraph.al_acyclic_graph_3())
        self.assertEqual({0, 1}, g.top_vertices)

    def test_find_bottom_vertices(self):
        g = Graph(CreateGraph.al_acyclic_graph_1())
        self.assertEqual({4, 7, 8}, g.bottom_vertices)

        g = Graph(CreateGraph.al_acyclic_graph_2())
        self.assertEqual({4, 9}, g.bottom_vertices)

        g = Graph(CreateGraph.al_acyclic_graph_3())
        self.assertEqual({6, 7}, g.bottom_vertices)

    def test_is_cyclic(self):
        g = Graph(CreateGraph.al_acyclic_graph_1())
        self.assertFalse(g.is_cyclic())

        g = Graph(CreateGraph.al_acyclic_graph_2())
        self.assertFalse(g.is_cyclic())

        g = Graph(CreateGraph.al_acyclic_graph_3())
        self.assertFalse(g.is_cyclic())

        g = Graph(CreateGraph.al_cyclic_graph_1())
        self.assertTrue(g.is_cyclic())

        g = Graph(CreateGraph.al_cyclic_graph_2())
        self.assertTrue(g.is_cyclic())

    def test_send_stream(self):
        g = Graph(CreateGraph.al_acyclic_graph_1())
        self.assertEqual(3, g.send_stream({0}))
        self.assertEqual(1, g.send_stream({3}))
        self.assertEqual(3, g.send_stream({0, 3}))

        g = Graph(CreateGraph.al_acyclic_graph_2())
        self.assertEqual(2, g.send_stream({0}))
        self.assertEqual(1, g.send_stream({3}))
        self.assertEqual(1, g.send_stream({10}))
        self.assertEqual(2, g.send_stream({0, 3, 10}))

        g = Graph(CreateGraph.al_acyclic_graph_5())
        self.assertEqual(3, g.send_stream({0}))
        self.assertEqual(3, g.send_stream({1}))
        self.assertEqual(5, g.send_stream({2}))
        self.assertEqual(2, g.send_stream({3}))
        self.assertEqual(3, g.send_stream({0, 1}))
        self.assertEqual(5, g.send_stream({0, 2}))
        self.assertEqual(5, g.send_stream({0, 3}))
        self.assertEqual(5, g.send_stream({1, 2}))
        self.assertEqual(5, g.send_stream({1, 3}))
        self.assertEqual(5, g.send_stream({2, 3}))
        self.assertEqual(5, g.send_stream({0, 1, 2}))
        self.assertEqual(5, g.send_stream({0, 1, 3}))
        self.assertEqual(5, g.send_stream({0, 2, 3}))
        self.assertEqual(5, g.send_stream({1, 2, 3}))
