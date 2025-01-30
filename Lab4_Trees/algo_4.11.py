
from random import randint
import sys
from sys import stdin

class Node:
    def __init__(self, value=None, priority=None, left=None, right=None, size=1):
        self.value: int = value
        self.priority: int = priority
        self.left: Node = left
        self.right: Node = right
        self.size: int = size
        self.max_value: int = value
        self.flag: int = 0

def push(node: Node):
    if node is not None and node.flag!=0:
        node.value += node.flag
        node.max_value += node.flag

        if node.left:
            node.left.flag += node.flag
        if node.right:
            node.right.flag += node.flag
        node.flag = 0

def size_of(node: Node) -> int:
    return node.size if node else 0

def recalc(node: Node):
    if node:
        
        push(node.left)
        push(node.right)

        node.size = size_of(node.left) + size_of(node.right) + 1
        node.max_value = node.value
        if node.left:
            node.max_value = max(node.max_value, node.left.max_value)
        if node.right:
            node.max_value = max(node.max_value, node.right.max_value)
    return node

def split(node: Node, x0: int):
    if not node:
        return None, None
    push(node)
    if size_of(node.left) < x0:
        a, b = split(node.right, x0 - size_of(node.left) - 1)
        node.right = a
        return recalc(node), b
    else:
        a, b = split(node.left, x0)
        node.left = b
        return a, recalc(node)

def merge(node1: Node, node2: Node) -> Node:
    
    if not node1 or not node2:
        return node1 if node1 else node2

    push(node1)
    push(node2)


    if node1.priority > node2.priority:
        node1.right = merge(node1.right, node2)
        return recalc(node1)
    else:
        node2.left = merge(node1, node2.left)
        return recalc(node2)

def add_number(node: Node, l: int, r: int, delta: int) -> Node:
    a, b = split(node, l)
    b, c = split(b, r - l + 1)
    if b:
        b.flag += delta
    return merge(a, merge(b, c))

def calculate_max(node: Node, l: int, r: int) -> int:
    a, b = split(node, l)
    b, c = split(b, r - l + 1)

    push(b)
    result = b.max_value
    node = merge(a, merge(b, c))
    return result

def print_tree(node: Node):
    if node is None:
        return

    push(node)
    print_tree(node.left)
    sys.stdout.write(f"{node.value} ")
    print_tree(node.right)




n = int(input())
array = [int(x) for x in input().split()]

root = None
for value in array:
    root = merge(root, Node(value=value, priority=randint(1, 2**31 - 1)))

m = int(input())
log = []


for _ in range(m):
    operation = input().split()
    
    match operation[0]:
        case 'm':
            i = int(operation[1])
            j = int(operation[2])
            log.append(calculate_max(root, i-1, j-1))
 
        case 'a':
            i = int(operation[1])
            j = int(operation[2])
            delta = int(operation[3])
            root = add_number(root, i-1, j-1, delta)
 
    
for i in range(len(log)):
    print(log[i], end = " ")
