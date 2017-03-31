import sys

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def validate_BST(root, min, max):
    if not root:
        return True

    if root.value <= min or root.value >= max:
        return False

    return validate_BST(root.left, min, root.value) and validate_BST(root.right, root.value, max)

def helper(root):
    return validate_BST(root, -sys.maxint, sys.maxint)

n1 = Node(1)
n0 = Node(0, n1)
assert(not helper(n0))

n1 = Node(1)
n0 = Node(0, None, n1)
assert(helper(n0))

n2 = Node(2)
n1 = Node(1, n2)
n0 = Node(0, None ,n1)
assert(not helper(n0))

n2 = Node(2)
n1 = Node(1, None, n2)
n0 = Node(0, None ,n1)
assert(helper(n0))
