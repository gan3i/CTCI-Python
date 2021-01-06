from typing import List
from collections import defaultdict
from queue import Queue


def get_build_order(projects: List[str], dependencies: List[List[str]]):
    in_degree_map = defaultdict(int)
    graph = defaultdict(set)
    build_graph(dependencies, graph, in_degree_map)
    q = Queue()
    for project in in_degree_map:
        if not in_degree_map[project]:
            q.put(project)
    result: List[str] = []
    visited = set()
    while not q.empty():
        curr = q.get()
        result.append(curr)
        visited.add(curr)
        for nhbr in graph[curr]:
            in_degree_map[nhbr] -= 1
            if in_degree_map[nhbr] == 0 and nhbr not in visited:
                q.put(nhbr)

    return None if len(result) != len(projects) else result


def build_graph(dependencies, graph, in_degree_map):
    for edge in dependencies:
        graph[edge[0]].add(edge[1])
        in_degree_map[edge[0]] += 0
        in_degree_map[edge[1]] += 1


proj = ["f", "d", "a", "h", "g", "k", "i","z"]
dep = [
    ["f", "d"],
    ["f", "a"],
    ["d", "a"],
    ["g", "a"],
    ["a", "h"],
    ["g", "h"],
    ["k", "i"],
    ["z", "g"],
    ["g", "z"]
]

print(get_build_order(proj, dep))
