# given an array of integers, find maximum product of three integers in an array


def max_product(arr):
    min1 = max1 = arr[0]
    min2 = float('inf')
    max2 = max3 = float('-inf')

    for i in range(1, len(arr)):
        if arr[i] > max1:
            max2 = max3 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max3 = max2
            max2 = arr[i]
        elif arr[i] > max3:
            max3 = arr[i]
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    return max(min1 * min2 * max1, max1 * max2 * max3)


print(max_product([-4, 1, -8, 9, 6]))
print(max_product([1, 7, 2, -2, 5]))