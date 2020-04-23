# Bartosz Szar
# buduję kopiec max z tablicy wzrostów
# ściągam z kopca p największych wzrostów
# ściągam z kopca q - p + 1 wzrostów i zapisuję je do tablicy wynikowej

def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(A, i):  # O(log(n)), A[0] = size
    l = left(i)
    r = right(i)
    if l <= A[0] and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A[0] and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(A[0] // 2, 0, -1):
        max_heapify(A, i)


def pop(A):
    tmp = A[1]
    A[1] = A[A[0]]
    A[0] -= 1
    max_heapify(A, 1)
    return tmp


def section(T, p, q):
    T.insert(0, len(T))  # ustawiam w pierwszym elemencie kopca ilość jego elementów
    build_max_heap(T)  # buduję strukturę kopca O(n)
    for i in range(p):  # usuwam p największych wzrostów z kopca - nie są mi potrzebne
        pop(T)
    result = []
    for j in range(q - p + 1):  #dodaję do tablicy wynikowej wzrosty, które w tablicy posortowanej malejąco znajdowałyby się po dindeksami od p do q
        result.append(pop(T))
    return result


# złożoność:
# - budowa kopca O(n)
# - sumarycznie q wywołań pop() O(nlog(n)) -> nalezy pamiętać o tym że każde z n wywołań heapify_max operuje na coraz mniejszym kopcu


#test
A = [6,4,5,7,2,1,3,9,13,29,34]
B = sorted([6,4,5,7,2,1,3,9,13,29,34], reverse=True)
print(section(A, 3, 4))
print(B)
