def possible(a, b, c, i, j, k):
    if k > len(a) - 1:
        return True
    if i > len(a) - 1 and j > len(b) - 1:
        return False
    if i <= len(a) - 1 and a[i] == c[k]:
        return possible(a, b, c, i + 1, j, k + 1)
    elif j <= len(b) - 1 and b[j] == c[k]:
        return possible(a, b, c, i, j + 1, k + 1)
    elif j > len(b) - 1:
        return possible(a, b, c, i + 1, j, k)
    elif i > len(a) - 1:
        return possible(a, b, c, i, j + 1, k)
    else:
        return possible(a, b, c, i + 1, j, k) or possible(a, b, c, i, j + 1, k)


def possible_wrapper(a, b, c):
    a = sorted(a)
    b = sorted(b)
    c = sorted(c)
    return possible(a, b, c, 0, 0, 0)

a = "aallmjvka"
b = "sgfdgskota"
c = "alamakota"
print(possible_wrapper(a,b,c))

