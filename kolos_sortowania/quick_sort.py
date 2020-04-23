def quick_sort(arr):
    lesser = []
    equal = []
    bigger = []
    if len(arr) > 1:
        pivot = arr[0]
        for el in arr:
            if el < pivot:
                lesser.append(el)
            elif el == pivot:
                equal.append(el)
            else:
                bigger.append(el)
        return quick_sort(lesser) + equal + quick_sort(bigger)
    return arr


array = [321, 3215, 235, 235, 13, 2134, 52, 235, 23, 1, 43, 23, 2335]
print(quick_sort(array))