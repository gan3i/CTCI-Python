from typing import Set, List
from collections import defaultdict


def get_build_order(projects: List[str], dependencies: List[List[str]]):
    visited = set()
    graph = build_graph(dependencies)
    result: List[str] = [None] * len(projects)
    end_index = [len(projects) - 1]
    for project in projects:
        if project not in visited:
            visited.add(project)
            recursion_stack = set()
            dfs(graph, project, visited, result, end_index, recursion_stack)

    return None if not result[0] else result


def dfs(graph, project, visited, result, end_index, recursion_stack):
    if not project:
        return True
    recursion_stack.add(project)
    for nhbr in graph[project]:
        if nhbr in recursion_stack:
            return False
        if nhbr not in visited:
            visited.add(nhbr)
            if not  dfs(graph, nhbr, visited, result, end_index, recursion_stack):
                return False
    result[end_index[0]] = (project)
    recursion_stack.remove(project)
    end_index[0] -= 1
    return True


def build_graph(dependencies):
    graph = defaultdict(set)
    for edge in dependencies:
        start = edge[0]
        end = edge[1]
        graph[start].add(end)
    return graph

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
