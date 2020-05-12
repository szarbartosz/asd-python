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


def kruskal_list(G):
    V = len(G)
    edges = []
    for u in range(V):
        for (v, w) in G[u]:
            edges.append((w, u, v))
    edges.sort()

    MST = []
    vertices = [None] * V
    for i in range(V):
        vertices[i] = Node(i)

    for e in edges:
        if find(vertices[e[1]]) != find(vertices[e[2]]):
            MST.append(e)
            union(vertices[e[1]], vertices[e[2]])

    print(f'minimal spanning tree contains those edges (weight, u, v): {MST}')
    return MST


G = [[(1, 1), (2, 3)], [(0, 1), (2, 1), (3, 4)], [(0, 3), (1, 1), (3, 2), (4, 7)], [(1, 4), (2, 2), (4, 9), (5, 3)], [(2, 7), (3, 9), (5, 8)], [(3, 3), (4, 8)]]
kruskal_list(G)
