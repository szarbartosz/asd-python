#bubbleSort - O(n^2)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#bubbleSort with flag - optimistic complexity O(n)
def bubbleSortFlag(arr):
    n = len(arr)
    sorted = True
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if sorted: break
        else: sorted = True


arr = [4,9,6,8,3,8,9,6,3,5,1,2]
print("unsorted array: ")
print(arr)
bubbleSort(arr)
print("sotred array: ")
print(arr)
