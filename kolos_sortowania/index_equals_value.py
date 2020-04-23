# Dana jest posortowana rosnąco tablica A wielkości n zawierająca parami różne liczby naturalne.
# Podaj algorytm, który sprawdzi, czy jest taki indeks i, że A[i] == i.
# Co zmieni się, jeżeli liczby będą po prostu całkowite, niekoniecznie naturalne?

# simple observation: sorted ascending different in pairs numbers -> for any index:
# numbers to the left of index < array[index], to the right > array[index]
# so, if the array[index] > index and such index' that array[index'] == index' exists - then it's on the left of index
# if the array[index] < index and such index' that array[index'] = index' exists - it's on the right of index
# we perform binary search with predefined conditions


def exists(arr):
    left = 0
    right = len(arr) - 1
    mid = (right - left) // 2
    while right >= left:
        if arr[mid] == mid:
            return True
        elif arr[mid] > mid:
            right = mid - 1
            mid = left + (right - left) // 2
        else:
            left = mid + 1
            mid = left + (right - left) // 2
    return False


array = [-2, -1, 0, 4, 5, 7]
print(exists(array))
