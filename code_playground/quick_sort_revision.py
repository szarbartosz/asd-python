def partition(arr, left, right):
    i = left - 1
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1


def quick_sort(arr, left, right):
    if right > left:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)

arr = [213,532,4,3214346,51,3,24,23,423,523]
quick_sort(arr,0,len(arr)-1)
print(arr)