class Node:
    def __init__(self, number, children):
        self.visited = False
        self.number = number
        self.children = children

    def __eq__(self, other):
        return self.number == other.number

def route_between_nodes(start, end):
    if not start:
        return False

    start.visited = True

    if start == end:
        return True

    result = False
    for node in start.children:
        if not node.visited:
            result = result or route_between_nodes(node, end)

    return result

# 1 -> 2 -> 3
n3 = Node(3, [])
n2 = Node(2, [n3])
n1 = Node(1, [n2])
assert(route_between_nodes(n1, n3))

# 1 -> 2 -> 3
n3 = Node(3, [])
n2 = Node(2, [n3])
n1 = Node(1, [n2])
assert(route_between_nodes(n2, n3))

# 1 -> 2 -> 3
n3 = Node(3, [])
n2 = Node(2, [n3])
n1 = Node(1, [n2])
assert(not route_between_nodes(n2, n1))

# 1 -> 2 -> 3
n3 = Node(3, [])
n2 = Node(2, [n3])
n1 = Node(1, [n2])
assert(not route_between_nodes(n3, n1))

# 1 -> 2 -> 3
n3 = Node(3, [])
n2 = Node(2, [n3])
n1 = Node(1, [n2])
assert(not route_between_nodes(n3, n2))

# 1 -> 2
#  \
#   -> 3 -> 4
n4 = Node(4, [])
n3 = Node(3, [n4])
n2 = Node(2, [])
n1 = Node(1, [n2, n3])
assert(route_between_nodes(n1, n4))

# 1 -> 2
#  \
#   -> 3 -> 4
n4 = Node(4, [])
n3 = Node(3, [n4])
n2 = Node(2, [])
n1 = Node(1, [n2, n3])
assert(route_between_nodes(n3, n4))

# 1 -> 2
#  \
#   -> 3 -> 4
n4 = Node(4, [])
n3 = Node(3, [n4])
n2 = Node(2, [])
n1 = Node(1, [n2, n3])
assert(not route_between_nodes(n2, n4))
