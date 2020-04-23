import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def print(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value, end=", ")
            tmp = tmp.next
        print("")

    def add(self, value):
        tmp = Node(value)
        tmp.next = self.head
        self.head = tmp
        tmp = None

    def get(self):
        tmp = self.head.value
        self.head = self.head.next
        return tmp


def split(num_lis):
    odd_lis = List()
    even_lis = List()
    while not num_lis.is_empty():
        tmp = num_lis.get()
        if tmp % 2 != 0:
            odd_lis.add(tmp)
        else:
            even_lis.add(tmp)
    return odd_lis, even_lis


if __name__ == '__main__':
    n = int(input("number of values to be insert into the list: "))
    a = int(input("lower bound: "))
    b = int(input("upper bound: "))

    lis = List()

    while n > 0:
        lis.add(random.randint(a, b))
        n -= 1

    print("input: ", end="")
    lis.print()

    odd, even = split(lis)

    print("odd: ", end="")
    odd.print()
    print("even: ", end="")
    even.print()
