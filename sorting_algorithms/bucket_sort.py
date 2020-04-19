def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucket_sort(arr):
    sections = len(arr)
    buckets = []
    for i in range(sections):
        buckets.append([])
    for el in arr:
        index = int(el * sections)
        buckets[index].append(el)
    for i in range(len(buckets)):
        insertion_sort(buckets[i])
    k = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    print(buckets)


arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.234, 0.513, 0.963, 0.123, 0.234, 0.043, 0.745, 0.514, 0.801, 0.734, 0.452, 0.401]
bucket_sort(arr)
print(arr)

