from unittest import TestCase

from Graph import Graph
from GraphRepr import GraphReprReader
from BranchAndBound import BranchAndBound


class TestBranchAndBound(TestCase):
    def test_solve_1(self):
        graph = Graph(GraphReprReader.read_from_file('TestFiles/Graph7.al'))
        bb = BranchAndBound(3, graph)
        solution = bb.solve()

        self.assertEqual([
            {1, 2, 3},
            {4},
            {5, 6, 7},
            {8, 9},
            {10, 11, 12}
        ], solution[0])
        self.assertEqual([
            {1, 2, 3},
            {4},
            {5, 6, 8},
            {7, 9},
            {10, 11, 12}
        ], solution[1])
