class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class List:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def add(self, val):
        tmp = Node(val)
        if self.isEmpty():
            self.first = tmp
            self.last = tmp
            return
        self.last.next = tmp
        self.last = tmp

    def make_from_array(self, arr):
        for i in range(len(arr)):
            self.add(arr[i])

    def print(self):
        tmp = self.first
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next


if __name__ == "__main___":
    lis = List()
    lis.add(1)
    lis.print()
    arr = [1, 2, 3]
    lis.make_from_array(arr)
    lis.print()
