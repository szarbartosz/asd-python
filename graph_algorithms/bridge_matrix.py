def find_bridge_matrix(G):
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    visit_time = [float('inf')] * V
    low = [float('inf')] * V
    time = 1

    def visit(u):
        visited[u] = True
        nonlocal time
        visit_time[u] = time
        low[u] = time
        time += 1

        for v in range(len(G[u])):
            if G[u][v] != 0:
                if not visited[v]:
                    parent[v] = u
                    visit(v)

                    low[u] = min(low[u], low[v])
                    if low[v] == visit_time[v]:
                        print(f'bridge: ({u}, {v})')
                elif v != parent[u]:
                    low[u] = min(low[u], visit_time[v])

    for i in range(V):
        if not visited[i]:
            visit(i)


G = [[0, 1, 0, 0, 0],
     [1, 0, 1, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 1, 1, 0, 1],
     [0, 0, 0, 1, 0]]

find_bridge_matrix(G)
