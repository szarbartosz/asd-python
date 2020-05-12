def dfs_matrix(G):
    V = len(G)
    visited = [False] * V
    parent = [None] * V

    def dfs_visit(u):
        visited[u] = True
        for i in range(V):
            if G[u][i] == 1:
                if not visited[i]:
                    parent[i] = u
                    dfs_visit(i)

    for i in range(V):
        if not visited[i]:
            dfs_visit(i)

    result = []
    for i in range(V):
        result.append(f'vertex: {i}  parent: {parent[i]}')
    return result


G = [[0,1,1,1,0,0,0,0],
     [0,0,0,1,0,0,0,0],
     [0,0,0,0,1,0,0,0],
     [0,0,0,0,0,1,1,0],
     [0,0,1,1,0,0,1,0],
     [0,0,0,0,0,0,0,1],
     [0,0,0,0,0,0,0,1],
     [0,0,0,0,0,0,0,0]]

arr = dfs_matrix(G)
for i in range(len(arr)):
    print(arr[i])
