# Given an array, find the smallest window in array sorting which will make the entire array sorted in increasing order...
import random

def smallest_window(arr):
    i = 1
    while arr[i] > arr[i - 1]:
        i += 1
    start = i
    while arr[i - 1] > arr[start]:
        i -= 1
    start = i

    j = len(arr) - 2
    while arr[j] < arr[j + 1]:
        j -= 1
    finish =  j
    while arr[j + 1] < arr[finish]:
        j += 1
    finish = j
    return i, j


if __name__ == '__main__':
    # n = int(input("number of values to be insert into the table: "))
    # a = int(input("lower bound: "))
    # b = int(input("upper bound: "))

    array = [1, 2, 3, 7, 5, 6, 4, 8]

    # while n > 0:
    #     array.append(random.randint(a, b))
    #     n -= 1

    if len(array) == 1:
        print("array which contains only one element is sorted: ", array)
        exit(0)

    is_sorted = True
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            is_sorted = False

    if is_sorted:
        print("array is already sorted: ", array)
    else:
        print("array before segregation: ", array)
        begin, end = smallest_window(array)
        print("sort the array from index {0} to {1}".format(begin, end))
