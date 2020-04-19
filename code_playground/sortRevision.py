def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def quickSort(arr):
    if len(arr) > 1:
        lesser = []
        equal = []
        grater = []
        pivot = arr[0]
        for value in arr:
            if value < pivot:
                lesser.append(value)
            elif value == pivot:
                equal.append(value)
            else:
                grater.append(value)
        return quickSort(lesser) + equal + quickSort(grater)
    return arr


def partition(arr, left, right):
    i = (left - 1)
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1


def quickSortPartition(arr, left, right):
    if right > left:
        mid = partition(arr, left, right)
        quickSortPartition(arr, left, mid - 1)
        quickSortPartition(arr, mid + 1, right)


def countingSort(arr, scope):
    result = []
    countElements = [0] * (scope + 1)
    for i in range(len(arr)):
        countElements[arr[i]] += 1
    for j in range(len(countElements)):
        k = countElements[j]
        while k > 0:
            result.append(j)
            k -= 1
    return result


def binarySearch(arr, val):
    left = 0
    right = len(arr) - 1
    while right >= left:
        mid = left + (right - left) // 2
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def binarySearchRecursive(arr, left, right, val):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == val:
            return mid
        elif val < arr[mid]:
            binarySearchRecursive(arr, left, mid - 1, val)
        else:
            binarySearchRecursive(arr, mid + 1, right, val)
    else:
        return -1

if __name__ == '__main__':
    arr = [313,5,312,6,3,734,3,24,3,14,34,6,46,7,425,32,31,24,12,364,73,6,89,76,827,45,1]
    quickSortPartition(arr,0,len(arr)-1)
    print("sprted array:\n", arr)
    print("key index:\n", binarySearch(arr,425))