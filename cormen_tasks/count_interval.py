# return how many elements of the given array are from the [a, b] interval
def count_interval(arr, a, b):
    k = max(arr)
    C = [0] * (k + 1)
    for i in range(len(arr)):
        C[arr[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    return C[b] - C[a - 1]


arr = [9, 5, 8, 6, 7, 2, 3, 4, 1]
tmp = count_interval(arr, 3, 7)
print(tmp)
