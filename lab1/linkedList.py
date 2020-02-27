class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#LinkedList traversal
def printList(head):
    if head is None:
        return None
    else:
        tmp = head
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next
        return None

#LinkedList insertion
def addToList(head, val):
    tmp = Node(val)
    tmp.next = head
    head = tmp

#LinkedList deletion

if __name__=='__main__':
    list = LinkedList()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    list.head.next = second
    second.next = third

    printList(list.head)
