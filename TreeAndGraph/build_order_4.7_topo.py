from typing import List, DefaultDict
from collections import defaultdict
from queue import Queue

def get_build_order(projects: List[str], dependencies: List[List[str]]):
    in_degree_map: DefaultDict[int] = defaultdict(int)
    graph: DefaultDict[set] = defaultdict(set)
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
            in_degree_map[nhbr] -=1
            if in_degree_map[nhbr] == 0 and nhbr not in visited:
                q.put(nhbr)

    return None if len(result) != len(projects) else result

def build_graph(dependencies, graph, in_degree_map):
    for edge in dependencies:
        start = edge[0]
        end = edge[1]

        graph[start].add(end)
        in_degree_map[start] +=0
        in_degree_map[end] +=1

proj = ["f","d","a","h","g","k","e"]
dep = [["f","d"],["f","a"],["d","a"],["g","a"],["a","h"],["g","h"],["k","i"]]

print(get_build_order(proj,dep))



