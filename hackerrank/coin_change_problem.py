# recursive
def recursive_get_ways(n, C, i):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if i <= 0 and n > 0:
        return 0
    return recursive_get_ways(n - C[i - 1], C, i) + recursive_get_ways(n, C, i - 1)


C = [1, 2, 3]
n = 4
print(recursive_get_ways(n, C, len(C)))


# bottom-up dp
def bottom_up_get_ways(n, C):
    F = [None] * (n + 1)
    for i in range(len(F)):
        F[i] = [0] * len(C)
    for i in range(len(C)):
        F[0][i] = 1
    for i in range(1, n + 1):
        for j in range(len(C)):
            if i - C[j] >= 0:
                x = F[i - C[j]][j]
            else:
                x = 0
            if j >= 1:
                y = F[i][j - 1]
            else:
                y = 0
            F[i][j] = x + y
    return F[n][len(C) - 1]


C = [1, 2, 3]
n = 4
print(bottom_up_get_ways(n, C))


# O(n) solution
def get_ways(n, C):
    F = [0] * (n + 1)
    F[0] = 1
    for i in range(len(C)):
        for j in range(C[i], n + 1):
            F[j] += F[j - C[i]]
    return F[n]


C = [1, 2, 3]
n = 4
print(get_ways(n, C))