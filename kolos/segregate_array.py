# Given an array consisting of positive and negative integers, segregate them in linear time and constant space.
# Output should print contain all negative numbers followed by all positive numbers

import random


def segregate(arr):
    pivot = -1
    for i in range(len(arr)):
        if arr[i] < 0:
            pivot += 1
            arr[pivot], arr[i] = arr[i], arr[pivot]
    return arr


if __name__ == '__main__':
    n = int(input("number of values to be insert into the table: "))
    a = int(input("lower bound: "))
    b = int(input("upper bound: "))

    array = []

    while n > 0:
        array.append(random.randint(a, b))
        n -= 1

    print("array before segregation: ", array)
    segregate(array)
    print("array after segregation: ", array)



