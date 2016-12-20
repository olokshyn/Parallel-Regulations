from unittest import TestCase

from Graph import Graph
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

    def test_find_top_vertices(self):
        g = Graph(CreateGraph.al_acyclic_graph_1())
        self.assertEqual({0, 3}, g.top_vertices)

        g = Graph(CreateGraph.al_acyclic_graph_2())
        self.assertEqual({0, 3, 10}, g.top_vertices)

        g = Graph(CreateGraph.al_acyclic_graph_3())
        self.assertEqual({0, 1}, g.top_vertices)

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
