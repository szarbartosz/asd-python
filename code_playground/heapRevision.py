def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


# max heap

def max_heapify(heap, i):
    l = left(i)
    r = right(i)
    if l <= heap[0] and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    if r <= heap[0] and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, largest)


def build_max_heap(arr):
    for i in range(arr[0] // 2, 0, -1):
        max_heapify(arr, i)


def heap_sort_asc(heap):
    for i in range(heap[0], 1, -1):
        heap[heap[0]], heap[1] = heap[1], heap[heap[0]]
        heap[0] -= 1
        max_heapify(heap, 1)


# min heap

def min_heapify(heap, i):
    l = left(i)
    r = right(i)
    if l <= heap[0] and heap[l] < heap[i]:
        smallest = l
    else:
        smallest = i
    if r <= heap[0] and heap[r] < heap[smallest]:
        smallest = r
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        min_heapify(heap, smallest)


def build_min_heap(arr):
    for i in range(arr[0] // 2, 0, -1):
        min_heapify(arr, i)


def heap_sort_dsc(heap):
    for i in range(heap[0], 1, -1):
        heap[1], heap[heap[0]] = heap[heap[0]], heap[1]
        heap[0] -= 1
        min_heapify(heap, 1)


if __name__ == '__main__':
    arr = [18, 2, 43, 52, 6, 1, 5, 645, 7, 457, 456, 3, 21, 34, 3, 5436, 436, 45, 5]

    build_max_heap(arr)
    print(arr)
    # heap_sort_asc(arr)
    # print(arr)

    build_min_heap(arr)
    print(arr)
    # heap_sort_dsc(arr)
    # print(arr)


