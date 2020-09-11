import numpy as np
import math


def binomial_coefficient(x, y):
    if y == 1 or y == x:
           return 1
    if y > x:
           return 0
    else:
        a = math.factorial(x)
        b = math.factorial(y)
        return a // (b*(x-y))


def hash_func(x, dict):
    return ((x + 21) * 37) % len(dict)


def find_pairs(arr):
    dict = [[]] * len(arr)

    for a in arr:
        hash = hash_func(a, dict)
        flag = False

        for tuple in dict[hash]:
            if tuple[0] == a:
                tuple[1] += 1
                flag = True

        if not flag:
            dict[hash].append([a, 1])



    result = 0
    for table in dict:
        for tuple in table:
            tmp = binomial_coefficient(tuple[1], 2)
            result += tmp
    return result


A = [3, 5, 6, 3, 3, 5]
print(find_pairs(A))
