def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def minHeapify(A, i):
    l = left(i)
    r = right(i)
    if l <= A[0] and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= A[0] and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        minHeapify(A, smallest)


def buildMinHeap(A):
    n = len(A)
    A.insert(0, n)
    for i in range(A[0] // 2, 0, -1):
        minHeapify(A, i)


def huffman_len(A):
    buildMinHeap(A)
    print(A)
    result = [None]
    while A[0] > 0:
        if A[0] == 1:
            result.append(A[1], 0)
        else:
            for i in range(2):
                result.append(A[1], 0)
                A[1] = A[A[0]]
                A[0] -= 1
                minHeapify(A, 1)




# elementarny test, powinien wypisać 2600
A = [ 200, 700, 180, 120, 70, 30]
print(huffman_len(A))