def bellman_ford_list(G, s):
    V = len(G)
    parent = [None] * V
    d = [float('inf')] * V
    d[s] = 0

    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    for i in range(V - 1):
        for i in range(V):
            for j in range(len(G[i])):
                relax(i, G[i][j][0], G[i][j][1])

    result = []
    for i in range(V):
        result.append(f'vertex: {i}  distance from source: {d[i]}')

    return result


# first element of the tuple is the id of the vertex - the second one is the weight of the edge
G = [[(1, 4), (2, 1)],
     [(3, 2)],
     [(1, 1), (3, 1)],
     [(4, 9)],
     []]

arr = bellman_ford_list(G, 0)
for i in range(len(arr)):
    print(arr[i])
