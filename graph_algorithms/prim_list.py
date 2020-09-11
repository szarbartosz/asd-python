from queue import PriorityQueue


def prim_list(G, s):
    V = len(G)
    Q = PriorityQueue()
    visited = [False] * V
    parent = [None] * V
    d = [float('inf')] * V
    d[s] = 0
    Q.put((d[s], s))

    def relax(u, v, w):
        if d[v] > w:
            d[v] = w
            parent[v] = u
            Q.put((d[v], v))

    while not Q.empty():
        (_, u) = Q.get()
        visited[u] = True
        for v in G[u]:
            if not visited[v[0]]:
                relax(u, v[0], v[1])
    result = ['MST:']
    sum = 0
    for i in range(V):
        if parent[i] is not None:
            for j in range(len(G[i])):
                if G[i][j][0] == parent[i]:
                    sum += G[i][j][1]
                    result.append('edge: ({}, {})   weight: {}'.format(parent[i], i, G[i][j][1]))
    result.append('sum of weights: {}'.format(sum))
    return result


G = [[(1, 4), (7, 8)],
     [(0, 4), (2, 8), (7, 11)],
     [(1, 8), (5, 4), (8, 2), (3, 7)],
     [(2, 7), (4, 9), (5, 14)],
     [(3, 9), (5, 10)],
     [(3, 14), (2, 4), (6, 2), (4, 10)],
     [(5, 2), (7, 1), (8, 6)],
     [(6, 1), (0, 8), (1, 11), (8, 7)],
     [(6, 6), (7, 7), (2, 2)]]

arr = prim_list(G, 1)
for i in range(len(arr)):
    print(arr[i])

H = [[(1, 28), (5, 10)],
     [(0, 28), (2, 16), (6, 14)],
     [(1, 16), (3, 12)],
     [(2, 12), (6, 18), (4, 22)],
     [(3, 22), (6, 24), (5, 25)],
     [(0, 10), (4, 25)],
     [(1, 14), (3, 18), (4, 24)]]

print('\n')
arr = prim_list(H, 5)
for i in range(len(arr)):
    print(arr[i])

I = [[(1, 3), (2, 1)],
     [(0, 3), (2, 1)],
     [(0, 1), (1, 1)]]

print('\n')
arr = prim_list(I, 0)
for i in range(len(arr)):
    print(arr[i])
