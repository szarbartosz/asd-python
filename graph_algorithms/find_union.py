class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


# in fact we are setting the parent attribute when we create a new Node so the below function is useless
def make_set(x):
    x.parent = x


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
    if x.rank == y.rank:
        y.rank += 1


# properties:
# rank of the tree is the upper bound of its height
# tree with the rank h has at most 2^h elements
# if the sum of all elements is n, the highest possible tree rank is <= ceil(log(n))

# complexity:
# find - O(log(n))
# union - O(log(n))

# complexity with path compression:
# amortized -> O(log*(n)) - iterated logarithm -> in practical use O(1) - iterated logarithm is <= 5 up to 2^65536

