from queue import PriorityQueue


def prim_matrix(G, s):
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
        for v in range(V):
            if G[u][v] > 0:
                if not visited[v]:
                    relax(u, v, G[u][v])
    result = ['MST:']
    sum = 0
    for i in range(V):
        if parent[i] is not None:
            sum += G[parent[i]][i]
            result.append('edge: ({}, {})   weight: {}'.format(parent[i], i, G[parent[i]][i]))
    result.append('sum of weights: {}'.format(sum))
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

arr = prim_matrix(G, 1)
for i in range(len(arr)):
    print(arr[i])


H = [[0, 28, 0, 0, 0, 10, 0],
     [28, 0, 16, 0, 0, 0, 14],
     [0, 16, 0, 12, 0, 0, 0],
     [0, 0, 12, 0, 22, 0, 18],
     [0, 0, 0, 22, 0, 25, 24],
     [10, 0, 0, 0, 25, 0, 0],
     [0, 14, 0, 18, 24, 0, 0]]

print('\n')
arr = prim_matrix(H, 5)
for i in range(len(arr)):
    print(arr[i])


I = [[0,3,1],
     [3,0,1],
     [1,1,0]]

print('\n')
arr = prim_matrix(I, 0)
for i in range(len(arr)):
    print(arr[i])
