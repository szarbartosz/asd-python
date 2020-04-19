def tasks(A):
    A.append((0,0)) #add 'guard' activity that will be used in activity_selector function
    A.sort(key=lambda tup: tup[1]) #sort activities by their end time
    n = len(A) - 1
    return activity_selector(A, 0, n)


def activity_selector(A, k, n):
    m = k + 1
    while m <= n and A[m][0] < A[k][1]:
        m += 1
    if m <= n:
        return 1 + activity_selector(A, m, n)
    else:
        return 0


A = [(0,10), (10,20), (5,15)]
print(tasks(A))

A = [(1,4), (3,5), (0,16), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]
print(tasks(A))

A = []
print(tasks(A))
