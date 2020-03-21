def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def heapifyMax(A, i):
    l = left(i)
    r = right(i)
    size = A[0]
    if l <= size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapifyMax(A,largest)

def heapifyMin(A, i):
    l = left(i)
    r = right(i)
    size = A[0]
    if l <= size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        heapifyMin(A,smallest)

def insertMax(maxHeap, val):
    maxHeap[0] += 1
    maxHeap.append(val)
    i = maxHeap[0]
    while i > 1 and maxHeap[i] > maxHeap[parent(i)]:
        maxHeap[i], maxHeap[parent(i)] = maxHeap[parent(i)], maxHeap[i]
        i = parent(i)

def insertMin(minHeap, val):
    minHeap[0] += 1
    minHeap.append(val)
    i = minHeap[0]
    while i > 1 and minHeap[i] < minHeap[parent(i)]:
        minHeap[i], minHeap[parent(i)] = minHeap[parent(i)], minHeap[i]
        i = parent(i)


def balanceHeaps(maxHeap, minHeap):
    if maxHeap[0] == minHeap[0] or maxHeap[0] == minHeap[0] + 1 or maxHeap[0] + 1 == minHeap[0]:
        return
    elif maxHeap[0] > minHeap[0]:
        insertMin(minHeap, maxHeap[1])
        size = maxHeap[0]
        maxHeap[1] = maxHeap[size]
        maxHeap[0] -= 1
        maxHeap.pop()
        heapifyMax(maxHeap, 1)
    else:
        insertMax(maxHeap, minHeap[1])
        size = minHeap[0]
        minHeap[1] = minHeap[size]
        minHeap[0] -= 1
        minHeap.pop()
        heapifyMin(minHeap, 1)

def getMedian(maxHeap, minHeap):
    if maxHeap[0] == 0 and minHeap[0] == 0:
        return 0
    elif maxHeap[0] == minHeap[0]:
        return (maxHeap[1] + minHeap[1]) / 2
    elif maxHeap[0] > minHeap[0]:
        return maxHeap[0]
    else:
        return minHeap[0]

def insert(maxHeap, minHeap, val):
    median = getMedian(maxHeap,minHeap)
    if val > median:
        insertMin(minHeap, val)
    else:
        insertMax(maxHeap, val)
    balanceHeaps(maxHeap, minHeap)


if __name__ == '__main__':
    maxHeap = [0]
    minHeap = [0]
    print(maxHeap,minHeap)
    insert(maxHeap,minHeap,1)
    insert(maxHeap,minHeap,3)
    insert(maxHeap,minHeap,4)
    insert(maxHeap,minHeap,17)
    insert(maxHeap,minHeap,8)
    insert(maxHeap,minHeap,11)
    insert(maxHeap,minHeap,2)
    print(maxHeap,minHeap)
    print('median:', getMedian(maxHeap,minHeap))
