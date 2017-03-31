def BST_sequence(root):
    if not root:
        return [[]]

    left_result_set = BST_sequence(root.left)
    right_result_set = BST_sequence(root.right)
    result = []
    for l in left_result_set:
        for r in right_result_set:
            result = result + weave(l, r)
    return [[root.value] + i for i in result]

def weave(arr1, arr2):
    if not arr1 and not arr2:
        return [[]]

    result1 = []
    if arr1:
        result1 = [[arr1[0]] + l for l in weave(arr1[1:], arr2)]

    result2 = []
    if arr2:
        result2 = [[arr2[0]] + l for l in weave(arr1, arr2[1:])]

    return result1 + result2

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

n0 = Node(0)
print BST_sequence(n0)

n1 = Node(1)
n3 = Node(3)
n2 = Node(2, n1, n3)
print BST_sequence(n2)
