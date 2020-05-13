# Nauczyłeś się właśnie piec nowe ciasto z wiśniami. W twoim cieście, między każdą parą wiśni przebiega słodka,
# żelkowa nitka. Jest on albo czarna (100g cukru), albo czerwona (200g cukru). Chciałeś poczęstować swoich
# znajomych, ale okazało się, że wszyscy są na diecie (przytyło im się przez kwarantannę) i nie zjedzą tak
# słodkiego ciasta. Mając listę par wisienek (długości P), pomiędzy którymi przebiega czarna nitka, liczbę
# wisienek (n, gdzie P<<n2), podaj jak najszybszy algorytm sprawdzający jaką minimalną zawartość cukru
# w cieście możesz uzyskać, usuwając dowolne nitki, ale pamiętając, że po usunięciu nitek musi między każdą parą
# wisienek istnieć przynajmniej jedna ścieżka.


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


def cake(n, black_edges):   #black_edges is a list of pairs (u, v) - vertices which are connected with black edge
    sugar = 0   #vertices of the graph
    cherries = [Node(i) for i in range(n)]
    for (u, v) in black_edges:
        if find(cherries[u]) != find(cherries[v]):
            sugar += 100
            union(cherries[u], cherries[v])

    components = [0] * n
    for cherry in cherries:
        components[find(cherry).id] += 1

    ssc = 0
    for i in range(n):
        if components[i] > 0:
             ssc += 1

    sugar += (ssc - 1) * 200

    print(f'the least sweet cake contains {sugar}g of sugar')


black_edges = [(0, 1), (1,2), (0,2), (0,3), (2,3), (4,5), (4,6), (5,6), (7,8), (8,9), (7,8), (8,9), (7,9), (9,7)]
cake(10, black_edges)