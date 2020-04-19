def longest_increasing_subsequence(A):
    n = len(A)
    F = [1] * n
    for i in range(n):
        for j in range(i):
            if A[i] > A[j] and F[i] < F[j] + 1:
                F[i] = F[j] + 1
    return max(F)


arr = [312, 3, 15431, 65, 234, 31, 6524, 342, 35431, 45, 23, 413, 23, 15, 323, 215, 412, 4432, 6523, 4, 3214, 124, 323]
print(longest_increasing_subsequence(arr))


