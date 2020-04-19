class Node:
    def __init__(self):
        self.next = None
        self.val = None

class Stack:
    def __init__(self):
        self.top = Node()

    def push(self, x):
        N = Node()
        N.val = x
        N.next = self.top
        self.top = N

    def pop(self):
        N = self.top
        self.top = N.next
        return N.val

    def is_empty(self):
        return self.top.next == None


S = Stack()
S.push(8)
S.push(9)
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())