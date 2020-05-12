def dfs_list(G):
    V = len(G)
    visited = [False] * V
    parent = [None] * V

    def dfs_visit(u):
        visited[u] = True
        for i in G[u]:
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


G = [[1,2,3], [3], [4], [5,6], [2,3,6], [7], [7], []]

arr = dfs_list(G)
for i in range(len(arr)):
    print(arr[i])