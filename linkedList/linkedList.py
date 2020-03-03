class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next

    def addToList(self, val):
        tmp = Node(val)
        tmp.next = self.head
        self.head = tmp

    def removeFromList(self, val):
        if self.head is None:
            return
        elif self.head.next is None:
            if self.head.data == val:
                toDelete = self.head
                self.head = self.head.next
                toDelete.next = None
                return
            else:
                return
        else:
            tmp = self.head
            while tmp.next is not None:
                if tmp.next.data == val:
                    toDelete = tmp.next
                    tmp.next = tmp.next.next
                    toDelete.next = None
                    return


if __name__=='__main__':
    lis = LinkedList()

    lis.addToList(1)
    lis.addToList(2)
    lis.addToList(3)

    lis.removeFromList(2)
    lis.printList()

    print(lis.isEmpty())