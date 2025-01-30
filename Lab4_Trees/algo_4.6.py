from random import randint
from sys import stdin

class Node:
    def __init__(self, value=None, priority=None, left=None, right=None, size = 1):
        self.value: int = value
        self.priority: int = priority
        self.left: Node = left
        self.right: Node = right
        self.size: int = size


def split(root: Node, x0: int):
    if root == None:
        return None, None

    if root.value < x0:
        a, b = split(root.right, x0)
        root.right = a
        return update_size(root), b
    elif root.value >= x0:
        a, b = split(root.left, x0)
        root.left = b
        return a, update_size(root) 


def merge(node_1: Node, node_2: Node):
    if node_1 == None:
        return node_2

    if node_2 == None:
        return node_1

    if node_1.priority < node_2.priority:
        node_1.right = merge(node_1.right, node_2)
        return update_size(node_1)
    else:
        node_2.left = merge(node_1, node_2.left)
        return update_size(node_2)

def insert(root: Node, x0: int):
        a, b = split(root, x0)
        c, d = split(b, x0 + 1)
        if c is None:
            c = Node(x0, randint(1, 2**31 - 1))        
        return merge(a, merge(c, d))

def delete(root: Node, x0: int):
    # в "a" все, что меньше икса, в b больше либо равно 
    a, b = split(root, x0)
    # с больше либо равно икса и меньше x + 1, значит это х!
    c, d = split(b, x0 + 1)
    c = None
    return merge(a, d)


def size_of(node: Node):
    if node is not None:
        return node.size
    else:
        return 0

def update_size(node: Node):
    if node is not None:
        node.size = size_of(node.left) + size_of(node.right) + 1
    return node

def find_k_i_max(root: Node, k: int):
    left_size = size_of(root.left)


    if k == left_size:
        return root.value
    elif k < left_size:
        return find_k_i_max(root.left, k)
    else:
        return find_k_i_max(root.right, k - left_size - 1)


root = None
n = int(input())
prev_operation = ''
size = 0

for i in range(n):
    operation = input().split()

    match operation[0]:
        case '1':
            if root == None:
                root = Node(int(operation[1]), randint(1, 2**31 - 1))
            else:
                root = insert(root, int(operation[1]))
            size += 1
        case '0':
            print(find_k_i_max(root, size - int(operation[1])))
        case '-1':
            root = delete(root, int(operation[1]))   
            size -= 1 

        