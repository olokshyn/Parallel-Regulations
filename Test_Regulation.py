from unittest import TestCase

from Graph import Graph
from Regulation import Regulation
import CreateGraph


class TestRegulation(TestCase):
    def test_build_s_lower(self):
        r = Regulation(Graph(CreateGraph.al_acyclic_graph_1()))
        self.assertEqual([
            {0, 3},
            {1, 2},
            {4, 5, 6, 7},
            {8}
        ], r.build_s_lower())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_1()), r.graph)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_2()))
        self.assertEqual([
            {0, 10, 3},
            {1, 2},
            {4, 5, 6, 7},
            {8},
            {9}
        ], r.build_s_lower())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_2()), r.graph)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_3()))
        self.assertTrue([
            {0, 1},
            {2},
            {3, 4},
            {5, 6},
            {7}
        ], r.build_s_lower())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_3()), r.graph)

    def test_build_s_upper(self):
        r = Regulation(Graph(CreateGraph.al_acyclic_graph_1()))
        self.assertEqual([
            {0},
            {1, 2},
            {3, 5, 6},
            {4, 7, 8}
        ], r.build_s_upper())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_1()), r.graph)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_2()))
        self.assertEqual([
            {0, 10},
            {1, 2},
            {3, 5, 6},
            {7, 8},
            {4, 9}
        ], r.build_s_upper())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_2()), r.graph)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_3()))
        self.assertTrue([
            {0, 1},
            {2},
            {3},
            {4, 5},
            {6, 7}
        ], r.build_s_upper())
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_3()), r.graph)

    def test_build_regulation(self):
        r = Regulation(Graph(CreateGraph.al_acyclic_graph_1()))
        self.assertEqual([
            {0, 3},
            {1, 2},
            {5, 6},
            {4, 8},
            {7}
        ], r.build_regulation(5, 2))
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_1()), r.graph)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_4()))
        self.assertEqual([
            {0, 10, 11},
            {1, 2, 12},
            {3, 4, 5},
            {6, 7, 13},
            {8},
            {9}
        ], r.build_regulation(6, 3))
        self.assertEqual(Graph(CreateGraph.al_acyclic_graph_4()), r.graph)

    def test_minimize_h(self):
        r = Regulation(Graph(CreateGraph.al_acyclic_graph_1()))
        h, regulation = r.minimize_h(5)
        self.assertEqual(2, h)
        self.assertEqual([
            {0, 3},
            {1, 2},
            {5, 6},
            {4, 8},
            {7}
        ], regulation)

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_4()))
        h, regulation = r.minimize_h(6)
        self.assertEqual(3, h)
        self.assertEqual([
            {0, 10, 11},
            {1, 2, 12},
            {3, 4, 5},
            {6, 7, 13},
            {8},
            {9}
        ], regulation)
        self.assertEqual(3, r.minimize_h(6)[0])

        r = Regulation(Graph(CreateGraph.al_acyclic_graph_5()))
        h, regulation = r.minimize_h(5)
        self.assertEqual(4, h)
        self.assertEqual([
            {0, 1, 2, 3},
            {4, 5, 6, 7},
            {8, 11},
            {9, 10, 12, 13},
            {14}
        ], regulation)
        h, regulation = r.minimize_h(6)
        self.assertEqual(3, h)
        self.assertEqual([
            {0, 1, 2},
            {3, 4, 5},
            {6, 7},
            {8, 11},
            {9, 10, 12},
            {13, 14}
        ], regulation)
