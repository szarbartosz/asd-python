def binary_search_iterative(arr, val):
    left = 0
    right = len(arr) - 1
    mid = (right - left) // 2
    while right >= left:
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            right = mid - 1
            mid = left + (right - left) // 2
        else:
            left = mid + 1
            mid = left + (right - left) // 2
    return None


def binary_search_recursive(arr, left, right, val):
    if right >= left:
        mid = left + (right - left) // 2
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            return binary_search_recursive(arr, left, mid - 1, val)
        else:
            return binary_search_recursive(arr, mid + 1, right, val)
    else:
        return None


array = [1, 13, 23, 23, 43, 52, 235, 235, 235, 321, 2134, 2335, 3215]
print(binary_search_iterative(array, 321))
print(binary_search_recursive(array, 0, len(array) - 1, 321))
