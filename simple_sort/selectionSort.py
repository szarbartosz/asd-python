#seletionSort - O(n^2)
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

arr = [4,9,6,8,3,8,9,6,3,5,1,2]
print("unsorted array: ")
print(arr)
selectionSort(arr)
print("sotred array: ")
print(arr)
