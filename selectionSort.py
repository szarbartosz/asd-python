#seletionSort - O(n^2)
def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp

arr = [4,9,6,8,3,8,9,6,3,5,1,2]

print("unsorted array: ")
print(arr)
selectionSort(arr)
print("sotred array: ")
print(arr)
