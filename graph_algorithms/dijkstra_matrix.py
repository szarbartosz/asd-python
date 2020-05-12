from queue import PriorityQueue


def dijkstra_matrix(G, s):
    V = len(G)
    Q = PriorityQueue()
    visited = [False] * V
    parent = [None] * V
    d = [float('inf')] * V
    d[s] = 0
    Q.put((d[s], s))

    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u
            Q.put((d[v], v))

    while not Q.empty():
        (_, u) = Q.get()
        visited[u] = True
        for v in range(V):
            if G[u][v] > 0:
                if not visited[v]:
                    relax(u, v, G[u][v])
    result = []
    for i in range(V):
        result.append(f'vertex: {i}  distance from source: {d[i]}')
    return result


G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
     [4, 0, 8, 0, 0, 0, 0, 11, 0],
     [0, 8, 0, 7, 0, 4, 0, 0, 2],
     [0, 0, 7, 0, 9, 14, 0, 0, 0],
     [0, 0, 0, 9, 0, 10, 0, 0, 0],
     [0, 0, 4, 14, 10, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 1, 6],
     [8, 11, 0, 0, 0, 0, 1, 0, 7],
     [0, 0, 2, 0, 0, 0, 6, 7, 0]]

arr = dijkstra_matrix(G, 1)
for i in range(len(arr)):
    print(arr[i])


H = [[0,3,1],
     [0,0,0],
     [0,1,0]]

print('\n')
arr = dijkstra_matrix(H, 0)
for i in range(len(arr)):
    print(arr[i])
