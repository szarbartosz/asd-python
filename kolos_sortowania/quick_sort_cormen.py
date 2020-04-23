def partition(arr, left, right):
    i = left - 1
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    if right > left:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


array = [321, 3215, 235, 235, 13, 2134, 52, 235, 23, 1, 43, 23, 2335]
fdsa = [(321, 1), (312, 21), (32131, 23), (1, 23)]
quick_sort(array, 0, len(array) - 1)
quick_sort(fdsa, 0, len(fdsa) - 1)
print(array)
print(fdsa)

