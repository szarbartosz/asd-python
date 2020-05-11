from queue import PriorityQueue


def dijkstra_list(G, s):
    V = len(G)
    Q = PriorityQueue()
    visited = [False] * V
    parent = [None] * V
    d = [float('inf')] * V
    d[s] = 0
    Q.put((d[s], s))

    def relax(u, v):
        for i in range(len(G[u])):
            if G[u][i][0] == v:
                w = G[u][i][1]
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u
            Q.put((d[v], v))

    while not Q.empty():
        (_, u) = Q.get()
        visited[u] = True
        for v in G[u]:
            if not visited[v[0]]:
                relax(u, v[0])
    result = []
    for i in range(V):
        result.append(f'vertex: {i}  distance from source: {d[i]}')
    return result


# first element of the tuple is the id of the vertex - the second one is the weight of the edge
G = [[(1,4), (2,1)],
     [(3,2)],
     [(1,1), (3,1)],
     [(4,9)],
     []]

arr = dijkstra_list(G, 0)
for i in range(len(arr)):
    print(arr[i])