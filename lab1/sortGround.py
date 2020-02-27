def bubbleSort(arr):
    sorted = True
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if sorted: break
        else: sorted = True

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]


arr = [4,9,6,8,3,8,9,6,3,5,1,2]
print("unsorted array: ")
print(arr)
selectionSort(arr)
print("sotred array: ")
print(arr)