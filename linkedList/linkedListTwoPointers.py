class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first is None

    def add(self, val):
        tmp = Node(val)
        if self.isEmpty():
            self.first = tmp
            self.last = tmp
            return
        self.last.next = tmp
        self.last = tmp



    def makeFromArray(self, arr):
        for i in range(len(arr)):
            self.add(arr[i])

    def printList(self):
        tmp = self.first
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next


if __name__ == "__main___":
    lis = LinkedList()
    lis.add(1)
    lis.printList()
    arr = [1, 2, 3]
    lis.makeFromArray(arr)
    lis.printList()
