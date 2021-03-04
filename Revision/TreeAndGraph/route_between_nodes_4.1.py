# Quwtions
# 1. is it a sparse graph or a dense graph (this helps to pick the data structure of the graph)
# 2. what should be the out put just a boolean indicating the path exists or not or the etire path
# 3. is it a connected graph or disconnected graph
# 4. directed or un-directed

# dicuss about the data structure you have choosen for graph and the difference between BFS and DFS

# Assumptions are
# it's sparse and connected graph, just have to return whetheer a path exists or not
# inputs are valid

from queue import Queue
from collections import defaultdict
from typing import DefaultDict, List


def bfs_search(graph: DefaultDict, start: str, end: str) -> bool:
    visited_nodes = set()
    q = Queue()
    q.put(start)
    while not q.empty():
        curr_node = q.get()
        if curr_node == end:
            return True
        else:
            visited_nodes.add(curr_node)
        for adj_node in graph[curr_node]:
            if adj_node not in visited_nodes:
                q.put(adj_node)

    return False


def search(graph: DefaultDict, start: str, end: str) -> bool:
    def dfs_search(graph, curr_node, end, visited):

        if curr_node == end:
            return True
        else:
            for adj_node in graph[curr_node]:
                if adj_node not in visited:
                    visited.add(curr_node)
                    return True if dfs_search(graph, adj_node, end, visited) else False

    return dfs_search(graph, start, end, set(start))


g = defaultdict(set)

g["A"] = {"B"}
g["B"] = {"D"}
g["C"] = {"A", "D"}
g["D"] = {"E"}
g["E"] = {"F"}


print(search(g, "A", "C"))
print(bfs_search(g, "B", "C"))
