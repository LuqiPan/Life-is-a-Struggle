class Node:
    def __init__(self, number, left=None, right=None):
        self.number = number
        self.left = left
        self.right = right

def list_of_depths(root):
    queue = []

    root.depth = 0
    queue.insert(0, root)

    result = []
    depth_so_far = -1
    while queue:
        curr = queue.pop()
        if depth_so_far != curr.depth:
            depth_so_far = curr.depth
            result.append([curr])
        else:
            result[-1].append(curr)

        if curr.left:
            curr.left.depth = curr.depth + 1
            queue.insert(0, curr.left)

        if curr.right:
            curr.right.depth = curr.depth + 1
            queue.insert(0, curr.right)

    return result

def print_list_of_depths(list):
    for l in list:
        print [node.number for node in l]

def helper(root):
    print_list_of_depths(list_of_depths(root))

n0 = Node(0)
helper(n0)

print '-----'

n2 = Node(2)
n1 = Node(1)
n0 = Node(0, n1, n2)
helper(n0)

print '-----'

n5 = Node(5)
n4 = Node(4)
n3 = Node(3, None, n5)
n2 = Node(2, n4)
n1 = Node(1, n3)
n0 = Node(0, n1, n2)
helper(n0)
