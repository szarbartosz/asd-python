# Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algorytm, który podzieli te liczby na n par w taki sposób,
# że podział będzie miał najmniejszą maksymalną sumę liczb w parze. Przykładowo, dla liczb (1, 3, 5, 9)  możemy mieć
# podziały ((1,3),(5,9)), ((1,5),(3,9)), oraz ((1,9),(3,5)). Sumy par dla tych podziałów to (4, 14),
# (6, 12) oraz (10, 8), w związku z tym maksymalne sumy to 14, 12 oraz 10. Wynika z tego, że ostatni podział ma
# najmniejszą maksymalną sumę.

# sort an array using quicksort, then pair up minimum and maximum at the time


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    if right > left:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


def find_mid_max_pairs(arr):
    result = []
    quick_sort(arr, 0, len(arr) - 1)
    i = 0
    j = len(arr) - 1
    for k in range(len(arr) // 2):
        result.append((arr[i], arr[j]))
        i += 1
        j -= 1
    return result


arr = [1, 9, 5, 3]
print(find_mid_max_pairs(arr))

# complexity:
# sort an array containing 2n elements with quicksort - 1 operation O(2nlog(2n)) -> O(nlog(n))
# connect two most distant element (current min and max) -> n operations O(1) -> O(n)