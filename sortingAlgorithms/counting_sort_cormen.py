def counting_sort(A):
    k = max(A)
    B = [0] * len(A)
    C = [0] * (k + 1)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    for i in range(len(A)):
        A[i] = B[i]


arr = [312, 532, 432, 32, 2, 12, 543, 532, 41, 321, 3, 214, 123, 1, 43, 214, 34, 32, 5, 3214, 2]
counting_sort(arr)
print(arr)
