def floyd_warshall(G):
    V = len(G)
    D = G
    for k in range(V):
        for i in range(V):
            for j in range(V):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


inf = float('inf')
G = [[0, 4, inf, inf, inf, inf, inf, 8, inf],
     [4, 0, 8, inf, inf, inf, inf, 11, inf],
     [inf, 8, 0, 7, inf, 4, inf, inf, 2],
     [inf, inf, 7, 0, 9, 14, inf, inf, inf],
     [inf, inf, inf, 9, 0, 10, inf, inf, inf],
     [inf, inf, 4, 14, 10, 0, 2, inf, inf],
     [inf, inf, inf, inf, inf, 2, 0, 1, 6],
     [8, 11, inf, inf, inf, inf, 1, 0, 7],
     [inf, inf, 2, inf, inf, inf, 6, 7, 0]]

arr = floyd_warshall(G)
for i in range(len(arr)):
    print(arr[i])