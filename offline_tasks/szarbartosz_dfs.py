# Proszę zaimplementować algorytm DFS dla grafu nieskierowanego reprezentowanego przez listy sąsiedztwa. Państwa implementacja powinna zwracać tablicę
# postaci [parent0, parent1, . . . , parentn−1], gdzie parent i to poprzednik wierzchołka i w drzewie DFS.
# Państwa kod powinien mieć następującą postać (będzie uruchamiany; proszę nie usuwać fragmentu testującego; sprawdzający może takżedołożyć swoje testy):

# G to lista list z informacją o istnieniu krawędzi
# G[i] to lista numerów wierzchołków, które są połączone
# krawędzią z wierzchołkiem i
# tu proszę umieścić swoją implementację

def DFS(G):
    V = len(G)
    visited = [False] * V
    parent = [None] * V

    def DFS_visit(u):
        visited[u] = True
        for i in range(len(G[u])):
            if not visited[G[u][i]]:
                parent[G[u][i]] = u
                DFS_visit(G[u][i])

    for i in range(V):
        if not visited[i]:
            DFS_visit(i)

    return parent


# elementarny test. Może wypisać np.
# [None, 0, 1, 2]
G = [[1,2],[0,2,3],[3,1,0],[1,2]]
print(DFS(G))