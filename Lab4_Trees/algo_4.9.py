from random import randint
import sys

class Node:
    def __init__(self, value=None, priority=None, left=None, right=None, size = 1, reversed = False):
        self.value: int = value
        self.priority: int = priority
        self.left: Node = left
        self.right: Node = right
        self.size: int = size
        self.reversed: bool = reversed # Флаг, что кажет нам, что поддерево нужно развернуть



def split(node: Node, x0: int):
    if node is None:
        return None, None
    push(node)
    if size_of(node.left) < x0:
        if node.right is None:
            return update_size(node), None

        a, b = split(node.right, x0 - size_of(node.left) - 1)
        node.right = a
        return update_size(node),b
    else:
        if node.left is None:
            return None, update_size(node)

        a, b = split(node.left, x0)
        node.left = b
        return a, update_size(node)
 

def merge(node1: Node, node2: Node):
    if not node1 or not node2:
        return node1 if node1 else node2
    
    push(node1)
    push(node2)

    if node1.priority > node2.priority:
        node1.right = merge(node1.right, node2)
        return update_size(node1)
    else:
        node2.left = merge(node1, node2.left)
        return update_size(node2)


def reverse_segment(node: Node, l: int, r: int):
    a, b = split(node, r + 1)
    c, d = split(a, l)

    # Применяем XOR
    if d:
        d.reversed ^= True
    return merge(merge(c, d), b)

def push(node: Node):
    if node and node.reversed:
        node.left, node.right = node.right, node.left
        if node.left:
            node.left.reversed ^= True
        if node.right:
            node.right.reversed ^= True
        node.reversed = False


def size_of(node: Node):
    if node is not None:
        return node.size
    else:
        return 0

def update_size(node: Node):
    if node is not None:
        node.size = size_of(node.left) + size_of(node.right) + 1
    return node

def print_tree(node: Node):
    if node is None:
        return
    push(node)  
    print_tree(node.left)
    sys.stdout.write(f"{node.value} ")
    print_tree(node.right)



input_data = [int(x) for x in input().split()]
n = input_data[0]
operations_count = input_data[1]

array = list(range(1, n + 1))

root = None
for i in range(n):
    root = merge(root, Node(i + 1, randint(1, 100000)))


for i in range(operations_count):
    operation = [int(x) for x in input().split()]
    l = operation[0]
    r = operation[1]

    root = reverse_segment(root, l-1, r-1)
print_tree(root)


