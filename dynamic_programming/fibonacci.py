def recursive_fib(n):
    if n <= 1:
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)

def dynamic_fib(n):
    if n < 2:
        return 1
    sequence = []
    sequence.append(1)
    sequence.append(1)
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[n]

def dynamic_fib_falisz(n):
    F = [1] * n + 1
    for j in range(2, n + 1):
        F[j] = F[j - 1] + F[j -2]
    return F[n]

def dynamic_better_fib_falisz(n):
    if n <= 1:
        return 1
    f1 = f2 = 1
    k = None
    for i in range(2, n + 1):
        k = f1 + f2
        f2 = k
        f1 = f2
    return k


F = [0] * 1000
F[0] = F[1] = 1
def fib_mem(n):
    if F[n] > 0:
        return F[n]
    else:
        F[n] = fib_mem(n - 1) + fib_mem(n - 2)
    return F[n]


def fib_mem(n):
    r = [0] * (n + 1)
    r[0] = r[1] = 1
    return fib_mem_aux(n, r)


def fib_mem_aux(n, r):
    if r[n] > 0:
        return r[n]
    r[n] = fib_mem_aux(n - 1, r) + fib_mem_aux(n - 2, r)
    return r[n]


a = dynamic_fib(120)
b = recursive_fib(20)
c = fib_mem(120)
print(a)
print(b)
print(c)