class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if node.key <= root.key:
            if root.left is None:
                root.left = node
                node.parent = root.left
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
                node.parent = root.right
            else:
                insert(root.right, node)

def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key <= root.key:
            root = root.left
        else:
            root = root.right
    return None

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            tmp = root.right
            root = None
            return tmp
        elif root.right is None:
            tmp = root.left
            root = None
            return tmp

        tmp = min(root.right)
        root.key = tmp.key
        root.right = delete(root.right, tmp.key)

    return root



def min(root):
    current = root
    while(current.left is not None):
        current = current.left
    return current

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, root.value)
        inorder(root.right)

root = BSTNode(20,"ma")
insert(root, BSTNode(10,"ala"))
insert(root, BSTNode(50,"psa"))
insert(root, BSTNode(30,"kota"))
insert(root, BSTNode(40,"i"))

inorder(root)
# print(find(root, 30).value)

delete(root, 30)
inorder(root)

# min = min(root)
# print(min.key)
