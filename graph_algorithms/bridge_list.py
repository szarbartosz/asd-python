def find_bridge_list(G):
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

        for v in G[u]:
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


G = [[1], [0,2,3], [1,3], [1,2,4], [3]]

find_bridge_list(G)
