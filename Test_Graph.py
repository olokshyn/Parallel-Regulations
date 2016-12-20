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

    def test_build_s_lower(self):
        g = Graph(CreateGraph.al_acyclic_graph_1())
        self.assertEqual([{0, 3}, {1, 2}, {4, 5, 6, 7}, {8}],
                         g.build_s_lower())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_1()), g)

        g = Graph(CreateGraph.al_acyclic_graph_2())
        self.assertEqual([{0, 10, 3}, {1, 2}, {4, 5, 6, 7},
                          {8}, {9}],
                         g.build_s_lower())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_2()), g)

        g = Graph(CreateGraph.al_acyclic_graph_3())
        self.assertTrue([{0, 1}, {2}, {3, 4}, {5, 6}, {7}],
                        g.build_s_lower())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_3()), g)

    def test_build_s_upper(self):
        g = Graph(CreateGraph.al_acyclic_graph_1())
        self.assertEqual([{0}, {1, 2}, {3, 5, 6}, {4, 7, 8}],
                         g.build_s_upper())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_1()), g)

        g = Graph(CreateGraph.al_acyclic_graph_2())
        self.assertEqual([{0, 10}, {1, 2}, {3, 5, 6},
                          {7, 8}, {4, 9}],
                         g.build_s_upper())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_2()), g)

        g = Graph(CreateGraph.al_acyclic_graph_3())
        self.assertTrue([{0, 1}, {2}, {3}, {4, 5}, {6, 7}],
                        g.build_s_upper())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_3()), g)
