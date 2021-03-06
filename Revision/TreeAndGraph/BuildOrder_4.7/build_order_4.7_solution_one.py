from __future__ import annotations
from typing import List


def find_build_order(projects: List[str], dependencies: List[List[str]]) -> List[str]:
    graph: Graph = build_graph(projects, dependencies)
    return order_projects(graph.get_nodes())


def build_graph(projects: List[str], dependencies: List[List[str]]) -> Graph:
    graph: Graph = Graph()
    for project in projects:
        graph.get_or_create_node(project)
    for dependency in dependencies:
        start: str = dependency[0]
        end: str = dependency[1]
        graph.add_edge(start, end)
    return graph


def order_projects(projects: List[Project]) -> List[Project]:
    order: List[Project] = [None] * len(projects)
    end_of_list: int = add_non_dependent(order, projects, 0)
    to_be_processed = 0
    while to_be_processed < len(order):
        current: Project = order[to_be_processed]
        if not current:
            return None
        children: List[Project] = current.get_children()
        for child in children:
            child.decrease_dependencies()
        end_of_list = add_non_dependent(order, children, end_of_list)
        to_be_processed += 1
    return order


def add_non_dependent(
    order: List[Project], projects: List[Project], offset: int
) -> int:
    for project in projects:
        if project.get_number_of_dependencies() == 0:
            order[offset] = project
            offset += 1
    return offset


class Project:
    def __init__(self, name: str):
        self._children: List[Project] = []
        self._map: dict[str, Project] = {}
        self._name: str = name
        self._dependencies: int = 0

    def add_neighbor(self, node: Project) -> None:
        if not node.get_name() in self._map:
            self._children.append(node)
            self._map[node.get_name()] = node
            node.increase_dependencies()

    def increase_dependencies(self) -> None:
        self._dependencies += 1

    def decrease_dependencies(self) -> None:
        self._dependencies -= 1

    def get_name(self) -> str:
        return self._name

    def get_children(self) -> List[Project]:
        return self._children

    def get_number_of_dependencies(self) -> int:
        return self._dependencies


class Graph:
    def __init__(self):
        self._nodes: List[Project] = []
        self._map: dict[str, Project] = {}

    def get_or_create_node(self, name: str) -> Project:
        if not name in self._map:
            node: Project = Project(name)
            self._nodes.append(node)
            self._map[name] = node
        return self._map[name]

    def add_edge(self, start: str, end: str) -> None:
        start_node: Project = self.get_or_create_node(start)
        end_node: Project = self.get_or_create_node(end)
        start_node.add_neighbor(end_node)

    def get_nodes(self):
        return self._nodes


proj = ["f", "d", "a", "h", "g", "k", "i", "z"]
dep = [
    ["f", "d"],
    ["f", "a"],
    ["d", "a"],
    ["g", "a"],
    ["a", "h"],
    ["g", "h"],
    ["k", "i"],
    ["z", "g"],
    # ["g", "z"]
]

print([proj.get_name() for proj in find_build_order(proj, dep)])
