class Stack:
    def __init__(self, n):
        self.S = [None] * n
        self.elements = 0
        self.n = n

    def push(self, x):
        self.S[self.elements] = x
        self.elements += 1

    def pop(self):
        self.elements -= 1
        return self.S[self.elements]

    def isEmpty(self):
        return self.elements == 0