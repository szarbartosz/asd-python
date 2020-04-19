class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def print(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next

    def add(self, val):
        tmp = Node(val)
        tmp.next = self.head
        self.head = tmp

    def remove(self, val):
        if self.head is None:
            return
        elif self.head.next is None:
            if self.head.data == val:
                to_delete = self.head
                self.head = self.head.next
                to_delete.next = None
                return
            else:
                return
        else:
            tmp = self.head
            while tmp.next is not None:
                if tmp.next.data == val:
                    to_delete = tmp.next
                    tmp.next = tmp.next.next
                    to_delete.next = None
                    return


if __name__=='__main__':
    lis = List()

    lis.add(1)
    lis.add(2)
    lis.add(3)

    lis.remove(2)
    lis.print()

    print(lis.is_empty())