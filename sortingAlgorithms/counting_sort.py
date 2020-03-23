def counting_sort(arr, scope):
    result = []
    count_el = [0] * (scope + 1)
    for i in range(len(arr)):
        count_el[arr[i]] += 1
    for j in range(len(count_el)):
        k = count_el[j]
        while k > 0:
            result.append(j)
            k -= 1
    return result


arr = [98, 34, 15, 65, 2, 4, 6, 94, 23, 54, 32, 6, 43]
arr = counting_sort(arr, 98)
print(arr)