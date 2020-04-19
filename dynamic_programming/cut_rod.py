import time

p = ['0', 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 31, 34, 41, 42, 50, 52, 52, 57, 60, 60, 60, 61, 62, 63, 65, 65, 67, 73,
     71, 74, 76]


# naive approach
def cut_rod(p, n):
    if n == 0:
        return 0
    q = -float('inf')
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


# begin = time.time()
# result = (cut_rod(p, 22))
# end = time.time()
# print('recursive cut_rod -> result: ', result, '\ntime: ', end - begin)


# memoized approach
def memoized_cut_rod(p, n):
    r = [-float('inf')] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


# begin = time.time()
# result = (memoized_cut_rod(p, 22))
# end = time.time()
# print('memoized cut_rod -> result: ', result, '\ntime: ', end - begin)


# bottom-up approach
def bottom_up_cut_rod(p, n):
    r = [None] * (n + 1)
    r[0] = 0
    for i in range(1, n + 1):
        q = -float('inf')
        for j in range(1, i + 1):
            q = max(q, p[j] + r[i - j])
        r[i] = q
    return r[n]


# begin = time.time()
# result = (bottom_up_cut_rod(p, 22))
# end = time.time()
# print('bottom_up cut_rod -> result: ', result, '\ntime: ', end - begin)


# cut rod with solution
def extended_bottom_up_cut_rod(p, n):
    r = [None] * (n + 1)
    s = [None] * (n + 1)
    r[0] = 0
    for i in range(1, n + 1):
        q = -float('inf')
        for j in range(1, i + 1):
            if q < p[j] + r[i - j]:
                q = p[j] + r[i - j]
                s[i] = j
        r[i] = q
    return r, s


def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n -= s[n]
    print(s)


# print_cut_rod_solution(p, 7)


# cut rod with solution -> considered cost of each cut (c)
def extended_bottom_up_cut_rod_with_cost(p, n, c):
    r = [None] * (n + 1)
    s = [None] * (n + 1)
    r[0] = 0
    for i in range(1, n + 1):
        q = -float('inf')
        for j in range(1, i + 1):
            if q < p[j] + r[i - j] - c:
                q = p[j] + r[i - j] - c
                s[i] = j
        r[i] = q
    return r, s


def print_cut_rod_solution_with_cost(p, n, c):
    r, s = extended_bottom_up_cut_rod_with_cost(p, n, c)
    while n > 0:
        print(s[n])
        n -= s[n]
    print(s)


print_cut_rod_solution_with_cost(p, 5, 4)
