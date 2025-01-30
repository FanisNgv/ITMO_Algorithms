from random import randint
import sys
from sys import stdin

class Node:
    def __init__(self, value=None, priority=None, left=None, right=None, size = 1, sum = 0):
        self.value: int = value
        self.priority: int = priority
        self.left: Node = left
        self.right: Node = right
        self.size: int = size
        self.sum: int = value


def split(node: Node, x0: int):
    if node is None:
        return None, None
    if size_of(node.left) < x0:
        if node.right is None:
            return update_size_and_sum(node), None

        a, b = split(node.right, x0 - size_of(node.left) - 1)
        node.right = a
        return update_size_and_sum(node),b
    else:
        if node.left is None:
            return None, update_size_and_sum(node)

        a, b = split(node.left, x0)
        node.left = b
        return a, update_size_and_sum(node)
 

def merge(node1: Node, node2: Node):
    if not node1 or not node2:
        return node1 if node1 else node2
    
    if node1.priority > node2.priority:
        node1.right = merge(node1.right, node2)
        return update_size_and_sum(node1)
    else:
        node2.left = merge(node1, node2.left)
        return update_size_and_sum(node2)


def size_of(node: Node):
    if node is not None:
        return node.size
    else:
        return 0



def get_sum(node: Node):
    if node is None:
        return 0
    else:
        return node.sum
 


def calculate_sum(node: Node, l: int, r: int):
    # вычленяем сплитом нужный нам диапазон
    a, b = split(node, l)
    b, c = split(b, r - l + 1)
 
    # считаем сумму
    ans = get_sum(b)
    
    # Объединение деревьев обратно
    node = merge(a, merge(b, c))
 
    return ans

def update_size_and_sum(node: Node):
    if node:
        node.size = size_of(node.left) + size_of(node.right) + 1
        node.sum = node.value + (node.left.sum if node.left else 0) + (node.right.sum if node.right else 0)
    return node

def set_value(node: Node, index: int, value: int):
    a, b = split(node, index)
    b, c = split(b, 1)
    b.value = value
    b.sum = value
    return merge(a, merge(b, c))

def print_tree(node: Node):
    if node is None:
        return
    print_tree(node.left)
    sys.stdout.write(f"{node.value} ")
    print_tree(node.right)

n = int(input())
array = [int(x) for x in input().split()]

root = None
for value in array:
    root = merge(root, Node(value, randint(1, 2**31 - 1)))


for operation in stdin:
    operation = operation.split()
    
    match operation[0]:
        case 'sum':
            i = int(operation[1])
            j = int(operation[2])
            sum = calculate_sum(root, i - 1, j - 1)
            print(sum)

        case 'set':
            i = int(operation[1])
            x = int(operation[2])

            set_value(root, i-1, x)
