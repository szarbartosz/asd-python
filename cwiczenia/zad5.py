def is_directed(G):
    for i in range(len(G)):
        for j in range(len(G[i])):
            if i not in G[G[i][j]]:
                return True
    return False

def is_directed(G):
    for i in range(len(G)):
        for j in range(len(G[i])):
            if i in G[G[i][j]]:
                G[G[i][j]].remove(i)
        else:
            return True
    return False
