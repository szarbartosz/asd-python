def countingSort(arr, scope):
    result = []
    countEl = [0] * (scope + 1)
    for i in range(len(arr)):
        countEl[arr[i]] += 1
    for j in range(len(countEl)):
        k = countEl[j]
        while k > 0:
            result.append(j)
            k -= 1
    return result


arr = [98, 34, 15, 65, 2, 4, 6, 94, 23, 54, 32, 6, 43]
arr = countingSort(arr, 98)
print(arr)