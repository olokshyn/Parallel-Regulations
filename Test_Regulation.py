from unittest import TestCase

from Graph import Graph
from Regulation import Regulation
import CreateGraph


class TestRegulation(TestCase):
    def test_build_s_lower(self):
        r = Regulation(Graph(CreateGraph.al_acyclic_graph_1()))
        self.assertEqual([{0, 3}, {1, 2}, {4, 5, 6, 7}, {8}],
                         r.build_s_lower())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_1()), r.graph)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_2()))
        self.assertEqual([{0, 10, 3}, {1, 2}, {4, 5, 6, 7},
                          {8}, {9}],
                         r.build_s_lower())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_2()), r.graph)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_3()))
        self.assertTrue([{0, 1}, {2}, {3, 4}, {5, 6}, {7}],
                        r.build_s_lower())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_3()), r.graph)

    def test_build_s_upper(self):
        r = Regulation(Graph(CreateGraph.al_acyclic_graph_1()))
        self.assertEqual([{0}, {1, 2}, {3, 5, 6}, {4, 7, 8}],
                         r.build_s_upper())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_1()), r.graph)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_2()))
        self.assertEqual([{0, 10}, {1, 2}, {3, 5, 6},
                          {7, 8}, {4, 9}],
                         r.build_s_upper())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_2()), r.graph)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_3()))
        self.assertTrue([{0, 1}, {2}, {3}, {4, 5}, {6, 7}],
                        r.build_s_upper())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_3()), r.graph)
