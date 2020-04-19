# Proszę zaimplementować algorytm BFS dla macierzowej reprezentacji grafu skierowanego. Państwa implementacja powinna zwracać tablicę postaci
# [(parent0, d0),(parent1, d1), . . . ,(parentn−1, dn−1)], gdzie parent i to poprzednik wierzchołka i na najkrótszej ścieżce z wierzchołka
# źródłowego a di to odległość i-go wierzchołka od żródłowe. Państwa kod powinien mieć następującą postać (będzie uruchamiany; proszę nie usuwać fragmentu
# testującego; sprawdzający może także dołożyć swoje testy):

# G to macierz opisująca graf: G[i][j]==1 jeśli jest
# wierzchołek z i do j. W przeciwnym razie G[i][j]=0
# s to numer wierzchołka źródłowego
# tu proszę umieścić swoją implementację

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

    def put(self, x):
        self.tail.next = Node(x)
        self.tail = self.tail.next

    def get(self):
        if self.head.next != self.tail:
            N = self.head.next
            self.head.next = N.next
            N.next = None
            return N.val
        else:
            N = self.head.next
            self.head.next = N.next
            self.tail = self.head
            return N.val

    def is_empty(self):
        return self.head == self.tail

def BFS(G, s):
    V = len(G[0])
    Q = Queue()
    visited = [False] * V
    parent = [None] * V
    d = [0] * V
    visited[s] = True

    Q.put(s)
    while not Q.is_empty():
        u = Q.get()
        for i in range(V):
            if G[u][i] == 1:
                if not visited[i]:
                    visited[i] = True
                    d[i] = d[u] + 1
                    parent[i] = u
                    Q.put(i)

    result = []
    for i in range(V):
        result.append((parent[i], d[i]))
    return result


# elementarny test, powinien wypisać
# [(None,0), (0,1), (0,1), (2,2)]
# lub
# [(None,0), (0,1), (0,1), (1,2)]
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
print(BFS(G,0))

#test dla grafu z wykładu
G = [[0,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,1,0],[0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
print(BFS(G,0))

#test dla grafu z przykładu - dodana krawędź z wierzchołka 1 do wierzchołka 0
G = [[0,1,1,1,0,0,0,0],[1,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,1,0],[0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
print(BFS(G,1))