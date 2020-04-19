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


if __name__ == '__main__':
    arr = [54,3234,32,54,54376,4,3,52,34,1,43,5,26,37,45,23,432,52,36]
    print(arr)
    quick_sort(arr,0,len(arr)-1)
    print(arr)