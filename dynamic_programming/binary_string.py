def count_strings(n):
    array = [[-1 for i in range(2)] for j in range(n + 1)]
    array[0][0], array[0][1], array[1][0], array[1][1] = 0, 0, 1, 1
    for i in range(2, n + 1):
        array[i][0] = array[i - 1][0] + array[i - 1][1]
        array[i][1] = array[i - 1][0]
    return array[n][0] + array[n][1], array


print(count_strings(5))