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
    for i in range(A[0] // 2, 0, -1):
        minHeapify(A, i)

def heapSortDESC(A):    #O(nlog(n))
    for i in range(A[0], 1, -1):
        A[A[0]], A[1] = A[1], A[A[0]]
        A[0] -= 1
        minHeapify(A,1)


if __name__ == '__main__':
    A = [11,6,4,5,7,2,1,3,9,13,29,34]
    buildMinHeap(A)
    print(A)
    heapSortDESC(A)
    print(A)