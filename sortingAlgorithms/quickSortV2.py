def quickSort(arr):
    lesser = []
    equal = []
    grater = []
    if len(arr) > 1:
        pivot = arr[0]
        for el in arr:
            if el < pivot:
                lesser.append(el)
            elif el == pivot:
                equal.append(el)
            else:
                grater.append(el)
        return quickSort(lesser) + equal + quickSort(grater)
    return arr