def partition_ternary(arr, left, right):
    pivot = arr[right]
    i = left - 1
    j = right
    k = left
    while k < j:
        if arr[k] < pivot:
            i += 1
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
        elif arr[k] > pivot:
            j -= 1
            arr[j], arr[k] = arr[k], arr[j]
        else:
            k += 1
    arr[j], arr[right] = arr[right], arr[j]
    return i + 1, j


def quick_sort_ternary(arr, left, right):
    if right > left:
        divider_left, divider_right = partition_ternary(arr, left, right)
        quick_sort_ternary(arr, left, divider_left - 1)
        quick_sort_ternary(arr, divider_right + 1, right)


arr = [321, 5321, 32, 531, 4123, 432, 5432, 7, 645, 64325243, 6, 4315, 432, 5, 34, 534, 52, 34, 324, 2]
quick_sort_ternary(arr, 0, len(arr) - 1)
print(arr)

