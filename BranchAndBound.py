from copy import deepcopy

from Regulation import Regulation
import Utils


class Branch(object):

    def __init__(self, l, s_lower, graph, regulation_part=None):
        self.l = l
        self.s_lower = s_lower
        self.graph = graph
        self.regulation_part = regulation_part
        self.branches = []
        self.canceled = False

    def add_branch(self, l, s_lower, graph, regulation_part):
        self.branches.append(Branch(l, s_lower, graph, regulation_part))


class BranchAndBound(object):

    def __init__(self, target_h, graph):
        self.target_h = target_h
        self.graph = graph
        self.top_branch = None

    def __count_length(self, graph, s_lower):
        n = len(graph.vertices)
        l_ = len(s_lower)
        l = n / float(self.target_h)
        if l - int(l) != 0.0:
            l = int(l) + 1
        else:
            l = int(l)
        return max(l_, l)

    def __build_branches(self, branch, level):
        if len(branch.graph.top_vertices) > self.target_h:
            combs = Utils.get_all_combinations(branch.graph.top_vertices,
                                               self.target_h)
        else:
            combs = [branch.graph.top_vertices]
        for comb in combs:
            temp_graph = deepcopy(branch.graph)
            for vertex in comb:
                del temp_graph.vertices[vertex]
            temp_graph.find_top_vertices()
            temp_graph.find_bottom_vertices()

            if len(temp_graph.vertices):
                r = Regulation(temp_graph)
                s_lower = r.build_s_lower()
                branch.add_branch(
                    self.__count_length(temp_graph, s_lower) + level,
                    s_lower,
                    temp_graph,
                    set(comb))
            else:
                branch.add_branch(
                    level,
                    None,
                    temp_graph,
                    set(comb)
                )

    def __build_tree(self):

        def _build_tree(branch, level):
            if not len(branch.graph.vertices):
                return

            self.__build_branches(branch, level)
            min_l = min([br.l for br in branch.branches])
            for br in branch.branches:
                if br.l == min_l:
                    _build_tree(br, level + 1)
                else:
                    br.canceled = True

        r = Regulation(self.graph)
        s_lower = r.build_s_lower()
        self.top_branch = Branch(self.__count_length(self.graph, s_lower),
                                 s_lower, self.graph)
        _build_tree(self.top_branch, 1)

    def solve(self):

        def collect_result(branch, result, regulation):
            regulation = list(regulation)
            regulation.append(branch.regulation_part)
            if not branch.branches:
                result.append(regulation)
            else:
                for br in branch.branches:
                    if not br.canceled:
                        collect_result(br, result, regulation)

        self.__build_tree()

        result = []
        regulation = []
        for br in self.top_branch.branches:
            collect_result(br, result, regulation)
        return result
