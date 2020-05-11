from queue import Queue


def bfs_list(G, s):
    V = len(G)
    Q = Queue()
    visited = [False] * V
    parent = [None] * V
    d = [float('inf')] * V
    visited[s] = True
    d[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in G[u]:
            if not visited[i]:
                visited[i] = True
                parent[i] = u
                d[i] = d[u] + 1
                Q.put(i)
    result = []
    for i in range(V):
        result.append(f'vertex: {i}  parent: {parent[i]}  distance from source: {d[i]}')
    return result


G = [[1,2,3], [3], [4], [5,6], [2,3,6], [7], [7], []]

arr = bfs_list(G, 0)
for i in range(len(arr)):
    print(arr[i])