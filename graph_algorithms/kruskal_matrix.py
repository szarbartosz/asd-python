class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
    if x.rank == y.rank:
        y.rank += 1


def kruskal_matrix(G):
    V = len(G)
    edges = []  # array of edges - data format: (weight, v1, v2)
    for u in range(V):
        for v in range(V):
            if G[u][v] != 0:
                edges.append((G[u][v], u, v))
    edges.sort()

    MST = []    # initializing the set that will contain the mst edges

    vertices = [None] * V
    for i in range(V):
        vertices[i] = Node(i)

    for e in edges:
        if find(vertices[e[1]]) != find(vertices[e[2]]):
            MST.append(e)
            union(vertices[e[1]], vertices[e[2]])

    print(f'minimal spanning tree contains those edges (weight, u, v): {MST}')
    return MST


G = [[0, 1, 3, 0, 0, 0],
     [1, 0, 1, 4, 0, 0],
     [3, 1, 0, 2, 7, 0],
     [0, 4, 2, 0, 9, 3],
     [0, 0, 7, 9, 0, 8],
     [0, 0, 0, 3, 8, 0]]

kruskal_matrix(G)
