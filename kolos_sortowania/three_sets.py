# Dane są trzy zbiory: A, B i C. Napisz algorytm, który powie, czy istnieje taka trójka a, b, c
# z odpowiednio A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników!

# sortujemy A i B
# ustawiamy sie wskaznikami na min A i max B


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quicksort(arr, left, right):
    if right > left:
        mid = partition(arr, left, right)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)


def exists(A, B, C):
    quicksort(A, 0, len(A) - 1)
    quicksort(B, 0, len(B) - 1)
    print(A)
    print(B)
    print(C)
    for c in C:
        i = 0
        j = len(B) - 1
        while i < len(A) and j >= 0:
            if c == A[i] + B[j]:
                return True
            elif c < A[i] + B[j]:
                j -= 1
            else:
                i += 1
    return False


A = [3, 41, 12, 41, 421, 2, 32]
B = [124, 4124, 12, 4, 321, 123]
C = [777, 555, 323]

print(exists(A, B, C))