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


def find_pairs(arr):
    dict = {}
    for a in arr:
        if not a in dict:
            dict[a] = 1
        else:
            dict[a] += 1
    result = 0
    for key in dict:
        tmp = binomial_coefficient(dict[key], 2)
        result += tmp
    return result


A = [3, 5, 6, 3, 3, 5]
print(find_pairs(A))
