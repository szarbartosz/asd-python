def topological_sort_matrix(G):
    V = len(G)
    visited = [False] * V
    stack = []

    def visit(u):
        visited[u] = True
        for v in G[u]:
            if G[u][v] != 0:
                if not visited[v]:
                    visit(v)
        stack.insert(0, u)

    for i in range(V):
        if not visited[i]:
            visit(i)

    print(f'topologically sorted vertices: {stack}')


H = [[0, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0]]

topological_sort_matrix(H)
