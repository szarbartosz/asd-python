# given an array of integers, find maximum product of two integers in an array


def max_product(arr):
    max1 = min1 = arr[0]
    max2 = float('-inf')
    min2 = float('inf')

    for i in range(1, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    return max(min1 * min2, max1 * max2)


print(max_product([-10, -3, 5, 6, -2]))
print(max_product([5, 3]))
