# Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, gdzie m jest znacznie mniejsze od n.
# Zaproponuj algorytm, który sprawdzi, czy zbiory są rozłączne.


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
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


# binary search that returns a boolean (True -> el is in arr)
def el_in_arr(arr, val):
    left = 0
    right = len(arr) - 1
    mid = (right - left) // 2
    while right >= left:
        if val == arr[mid]:
            return True
        elif val < arr[mid]:
            right = mid - 1
            mid = left + (right - left) // 2
        else:
            left = mid + 1
            mid = left + (right - left) // 2
    return False


# |arr1| >> |arr2| - more efficient
def are_disjoint(arr1, arr2):
    quick_sort(arr2, 0, len(arr2) - 1)
    for el in arr1:
        if el_in_arr(arr2, el):
            return False
    return True


n = [321, 3215, 235, 235, 13, 2134, 52, 235, 23, 1, 43, 23, 2335, 623, 41, 2, 15, 2732, 745, 6345, 652, 36]
m = [412, 214, 312, 4, 14]

print(are_disjoint(n, m))

# complexity:
# quick_sort: O(mlog(m))
# n calls of el_in_arr (binary search call on m): O(nlog(m))
# overall complexity: mlog(m) + nlog(m) = O((m + n)log(m))
