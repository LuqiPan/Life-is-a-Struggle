def first_common_ancestor(root, p, q):
    global p_found
    global q_found
    left = None
    if root.left:
        left = first_common_ancestor(root.left, p, q)

    if root == p:
        p_found = True
        return p

    if root == q:
        q_found = True
        return q

    right = None
    if root.right:
        right = first_common_ancestor(root.right, p, q)

    if not left and not right:
        return None

    if not left:
        return right

    if not right:
        return left

    return root

def first_common_ancestor_helper(root, p, q):
    global p_found
    global q_found
    p_found = False
    q_found = False
    result = first_common_ancestor(root, p, q)
    if p_found and q_found:
        return result

    return None

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.value == other.value

n2 = Node(2)
n1 = Node(1)
n0 = Node(0, n1, n2)
np = Node(4)
nq = Node(5)
print first_common_ancestor_helper(n0, np, nq)
print first_common_ancestor_helper(n0, np, n1)
print first_common_ancestor_helper(n0, n1, nq)
print first_common_ancestor_helper(n0, n2, n1).value

n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1)
n0 = Node(0, n1, n2)
print first_common_ancestor_helper(n0, n3, n2).value

n4 = Node(4)
n3 = Node(3)
n2 = Node(2, None, n4)
n1 = Node(1, n3)
n0 = Node(0, n1, n2)
print first_common_ancestor_helper(n0, n4, n3).value
