def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def maxHeapify(A, i): #O(log(n)), A[0] = size
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
        maxHeapify(A, largest)

def buildMaxHeap(A):
    for i in range(A[0] // 2, 0, -1):
        maxHeapify(A, i)

def heapSortASC(A): #O(nlog(n))
    for i in range(A[0], 1, -1):
        A[A[0]], A[1] = A[1], A[A[0]]
        A[0] -= 1
        maxHeapify(A,1)


if __name__ == '__main__':
    A = [11,6,4,5,7,2,1,3,9,13,29,34]
    buildMaxHeap(A)
    print(A)
    heapSortASC(A)
    print(A)