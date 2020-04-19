def counting_sort(arr, exp):
    B = [0] * len(arr)
    C = [0] * 10
    for i in range(len(arr)):
        index = (arr[i] // exp) % 10
        C[index] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        index = (arr[i] // exp) % 10
        B[C[index] - 1] = arr[i]
        C[index] -= 1
    for i in range(len(arr)):
        arr[i] = B[i]


def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value / exp > 0:
        counting_sort(arr, exp)
        exp *= 10


arr = [321,432543,5,2134,1,3,213,21,31,23,12,312,541,4,12,321,312,321,3,231]
radix_sort(arr)
print(arr)