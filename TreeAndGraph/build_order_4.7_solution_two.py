from __future__ import annotations
from typing import List
from queue import LifoQueue
from enum import Enum


def find_build_order(projects: List[str], dependencies: List[List[str]]) -> List[str]:
    graph: Graph = build_graph(projects, dependencies)
    return order_projects(graph.get_nodes())


def order_projects(projects: List[Project]) -> List[Project]:
    order = LifoQueue()
    for project in projects:
        if project.get_state() == State.BLANK:
            if not doDFS(project, order):
                return None
    return order


def doDFS(project, order):
    if project.get_state() == State.PARTIAL:
        return False
    if project.get_state() == State.BLANK:
        project.set_state(State.PARTIAL)
        for child in project.get_children():
            if not doDFS(child, order):
                return False
        project.set_state(State.COMPLETE)
        order.put(project)
    return True


# Same as previous Soltuion
def build_graph(projects: List[str], dependencies: List[List[str]]) -> Graph:
    graph: Graph = Graph()
    for project in projects:
        graph.get_or_create_node(project)
    for dependency in dependencies:
        start: str = dependency[0]
        end: str = dependency[1]
        graph.add_edge(start, end)
    return graph


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


class Project:
    def __init__(self, name: str):
        self._children: List[Project] = []
        self._map: dict[str, Project] = {}
        self._name: str = name
        self._dependencies: int = 0
        self._state = State.BLANK

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

    def get_state(self):
        return self._state

    def set_state(self, state: State):
        self._state = state


class State(Enum):
    COMPLETE = 1
    PARTIAL = 2
    BLANK = 3


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

result = find_build_order(proj, dep)
lis = []
while not result.empty():
    lis.append(result.get().get_name())
print(lis)
