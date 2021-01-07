from collections import defaultdict

def find_build_order(projects, dependencies):
    visited, order = set(), []
    graph = build_graph(dependencies)
    for project in projects:
        if project not in visited:
            visited.add(project)
            recursion_stack = set()
            if not dfs(graph, project, visited, order, recursion_stack):
                return None
    return list(reversed(order))


def dfs(graph, project, visited, order, recursion_stack):
    recursion_stack.add(project)
    for nhbr in graph[project]:
        if nhbr in recursion_stack:
            return False
        if nhbr not in visited:
            visited.add(nhbr)
            if not dfs(graph, nhbr, visited, order, recursion_stack):
                return False
    order.append(project)
    recursion_stack.remove(project)
    return True


def build_graph(dependencies):
    graph = defaultdict(set)
    for edge in dependencies:
        start, end = edge[0], edge[1]
        graph[start].add(end)
    return graph


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
    ["h", "f"]
]

print(find_build_order(proj, dep))
