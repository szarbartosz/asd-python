# Bartosz Szar

# tworzę tablicę struktur w której oprócz oryginalnych liczb przechowuję także ilość zawieranych przez nie cyfr jednokrotnych i liczb wielokrotnych
# następnie sortuję liczby po ilości zawartych w nich cyfr wielokrotnych
# w ostatnim kroku sortuję malejąco po liczbie jej cyfr jednokrotnych

# tworzę strukturę w której oprócz liczb przechowuję także ilość posiadanych przez nią liczb jednokrotnych i wielokrotnych
class Node:
    def __init__(self, number):
        self.number = number
        self.single = 0
        self.multi = 0


#dla każdej liczby obliczam ile znajduje się w niej liczb jednokrotnych i wielokrotnych
def calculate_single_multi(node):
    tmp = node.number
    t = [0] * 10
    while tmp > 0:
        unit = tmp % 10
        t[unit] += 1
        tmp //= 10
        t[unit] += 1
    single = multi = 0
    for i in range(len(t)):
        if t[i] == 1:
            single += 1
        if t[i] >= 2:
            multi += 1
    return single, multi


def mergesort_multi(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergesort_multi(left)
        mergesort_multi(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i].multi < right[j].multi:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def mergesort_single_desc(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergesort_multi(left)
        mergesort_multi(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i].single > right[j].single:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def pretty_sort(T):
    for i in range(len(T)):
        tmp = Node(T[i])
        T[i] = tmp
    for i in range(len(T)):  # uaktualniam tablicę - zmieniam liczbę na strukturę zawierającą oprócz niej jeszcze ilość liczb jednokrotnych i wielokrotnych
        T[i].single, T[i].multi = calculate_single_multi(T[i])
    mergesort_multi(T) # sortuję stabilnie tablicę T po ilości cyfr wielokrotnych
    mergesort_single_desc(T) # sortuję stabilnie tablicę T po ilosći cyfr jednokrotnych malejąco
    return T

# złożoność:
# mergesort - O(nlog(n))
