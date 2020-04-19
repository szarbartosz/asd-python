class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

    def put(self, x):
        self.tail.next = Node(x)
        self.tail = self.tail.next

    def get(self):
        if self.head.next != self.tail:
            N = self.head.next
            self.head.next = N.next
            N.next = None
            return N.val
        else:
            N = self.head.next
            self.head.next = N.next
            self.tail = self.head
            return N.val

    def is_empty(self):
        return self.head == self.tail


Q = Queue()
Q.put(8)
Q.put(9)
print(Q.get())
print(Q.is_empty())
print(Q.get())
print(Q.is_empty())