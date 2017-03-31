class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def _check_balanced(root):
    if (not root.left) and (not root.right):
        return 1

    left_height = 0
    if root.left:
        left_height = _check_balanced(root.left)

    right_height = 0
    if root.right:
        right_height = _check_balanced(root.right)

    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1

    return max([left_height, right_height]) + 1

def check_balanced(root):
    return _check_balanced(root) != -1

n0 = Node()
assert(check_balanced(n0))

n2 = Node()
n1 = Node()
n0 = Node(n1, n2)
assert(check_balanced(n0))

n4 = Node()
n3 = Node(n4)
n2 = Node(n3)
n1 = Node()
n0 = Node(n1, n2)
assert(not check_balanced(n0))
