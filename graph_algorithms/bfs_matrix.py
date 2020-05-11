from queue import Queue


def bfs_matrix(G, s):
    V = len(G)
    Q = Queue()
    visited = [False] * V
    parent = [None] * V
    d = [float('inf')] * V
    visited[s] = True
    parent[s] = None
    d[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(V):
            if G[u][i] == 1:
                if not visited[i]:
                    visited[i] = True
                    parent[i] = u
                    d[i] = d[u] + 1
                    Q.put(i)
    result = []
    for i in range(V):
        result.append(f'vertex: {i}  parent: {parent[i]}  distance from source: {d[i]}')
    return result


G = [[0,1,1,1,0,0,0,0],
     [0,0,0,1,0,0,0,0],
     [0,0,0,0,1,0,0,0],
     [0,0,0,0,0,1,1,0],
     [0,0,1,1,0,0,1,0],
     [0,0,0,0,0,0,0,1],
     [0,0,0,0,0,0,0,1],
     [0,0,0,0,0,0,0,0]]

arr = bfs_matrix(G, 0)
for i in range(len(arr)):
    print(arr[i])

