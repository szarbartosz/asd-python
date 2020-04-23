# Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimum (array-based heap).
# Mając daną liczbę rzeczywistą x sprawdź, czy k-ty najmniejszy element jest większy lub równy x.

# naive approach - perform get_mid k times (klog(n)) and check weather the kth smallest element is gte x
# efficient approach - perform heap-tree traversal - if fond at least k nodes which value < x - return false
def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


glob = 0


def traverse(heap, index, k, x):
    if heap[index] < x:
        global glob
        glob += 1
        print('glob:', glob, ' el:', heap[index], ' x:', x)
        if glob >= k:
            return False
        return traverse(heap, left(index), k, x)
        return traverse(heap, right(index), k, x)
    return True


def is_kth_element_grater_than_x(heap, k, x):
    return traverse(heap, 1, k, x)


arr = [11, 1, 2, 3, 7, 4, 5, 6, 9, 13, 29, 34]
# [1, 2, 3, 4, 5, 6, 7, 9, 13, 29, 34]
print(is_kth_element_grater_than_x(arr, 7, 16))