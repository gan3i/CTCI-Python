
#Quwtions 
# 1. is it a sparse graph or a dense graph (this helps to pick the data structure of the graph)
# 2. what should be the out put just a boolean indicating the path exists or not or the etire path
# 3. is it a connected graph or disconnected graph
# 4. directed or un directed 

# dicuss about the data structure you have choosen for graph and the difference between BFS and DFS

#Assumptions are
# it's sparse and connected graph, just have to return whetheer a path exists or not
# inputs are valid
from queue import Queue
def search(graph, start, end):

    if start == end:
        return True

    visited = set()
    q = Queue()
    q.put(start)

    while not q.empty():

        curr = q.get()
        visited.add(curr)
        
        for adj in graph[curr]:
            if adj not in visited:
                if adj == end:
                    return True
                else:
                    q.put(adj)

    return False

from collections import defaultdict
g = defaultdict(set)

g[1] = {2,3,4}
g[2] = {5,3}
g[3] = {4,1}


print(search(g, 3,5))



