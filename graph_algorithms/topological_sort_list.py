def topological_sort_list(G):
    V = len(G)
    visited = [False] * V
    stack = []

    def visit(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visit(v)
        stack.insert(0, u)

    for i in range(V):
        if not visited[i]:
            visit(i)

    print(f'topologically sorted vertices: {stack}')


G = [[1, 2, 4], [2, 3], [], [5, 6], [3], [], []]
topological_sort_list(G)
