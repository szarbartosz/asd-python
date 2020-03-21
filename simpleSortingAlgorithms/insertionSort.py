#insertionSort - O(n^2)
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [4,9,6,8,3,8,9,6,3,5,1,2]
print("unsorted array: ")
print(arr)
insertionSort(arr)
print("sotred array: ")
print(arr)