#bubbleSort - O(n^2)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

arr = [4,9,6,8,3,8,9,6,3,5,1,2]

print("unsorted array: ")
print(arr)
bubbleSort(arr)
print("sotred array: ")
print(arr)
