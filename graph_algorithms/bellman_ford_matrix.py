def bellman_ford_matrix(G, s):
    V = len(G)
    parent = [None] * V
    d = [float('inf')] * V
    d[s] = 0

    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    for i in range(V - 1):
        for u in range(V):
            for v in range(V):
                relax(u, v, G[u][v])

    for u in range(V):
        for v in range(V):
            if d[v] > d[u] + G[u][v]:
                return False, None

    result = []
    for i in range(V):
        result.append(f'vertex: {i}  distance from source: {d[i]}')
    return True, result


G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
     [4, 0, 8, 0, 0, 0, 0, 11, 0],
     [0, 8, 0, 7, 0, 4, 0, 0, 2],
     [0, 0, 7, 0, 9, 14, 0, 0, 0],
     [0, 0, 0, 9, 0, 10, 0, 0, 0],
     [0, 0, 4, 14, 10, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 1, 6],
     [8, 11, 0, 0, 0, 0, 1, 0, 7],
     [0, 0, 2, 0, 0, 0, 6, 7, 0]]

flag, arr = bellman_ford_matrix(G, 0)
if flag:
    for i in range(len(arr)):
        print(arr[i])
else:
    print("graph has negative cycle")