from random import randint
from sys import stdin
 
class Node:
    def __init__(self, value=None, priority=None, left=None, right=None, sum = 0):
        self.value: int = value
        self.priority: int = priority
        self.left: Node = left
        self.right: Node = right
        # сумма поддерева
        self.sum: int = value
        
def split(root: Node, x0: int):
    if root == None:
        return None, None
    if root.value < x0:
        a, b = split(root.right, x0)
        root.right = a
        update_sum(root)
        return root, b
    elif root.value >= x0:
        a, b = split(root.left, x0)
        root.left = b
        update_sum(root)
        return a, root 
 
def merge(node_1: Node, node_2: Node):
    if node_1 == None:
        return node_2
 
    if node_2 == None:
        return node_1
 
    if node_1.priority < node_2.priority:
        node_1.right = merge(node_1.right, node_2)
        update_sum(node_1)
        return node_1
    else:
        node_2.left = merge(node_1, node_2.left)
        update_sum(node_2)
        return node_2
 
def insert(root: Node, x0: int):
        a, b = split(root, x0)
        c, d = split(b, x0 + 1)

        if c is None:
            c = Node(x0, randint(1, 2**31 - 1))        
        return merge(a, merge(c, d))
 
def get_sum(node: Node):
    if node is None:
        return 0
    else:
        return node.sum
 
 
def update_sum(node: Node):
    if node is not None:
        left_sum = get_sum(node.left) if node.left is not None else 0
        right_sum = get_sum(node.right) if node.right is not None else 0 
        node.sum = node.value + left_sum + right_sum
 
def calculate_sum(node: Node, l: int, r: int):
    # вычленяем сплитом нужный нам диапазон
    a, b = split(node, l)
    b, c = split(b, r + 1)
 
    # считаем сумму
    ans = get_sum(b)
    
    # Объединение деревьев обратно
    node = merge(a, merge(b, c))
 
    return ans
 

power = int(10e8)
root = None
n = int(input())
prev_operation = ''
 
 
for operation in stdin:
    operation = operation.split()
 
    match operation[0]:
        case '+':
            if root == None:
                root = Node(int(operation[1]), randint(1, 2**31 - 1))
            else:
                if prev_operation == '?':
                    root = insert(root, int((int(operation[1]) + sum) % power))
                else:
                    root = insert(root, int(operation[1]))
            prev_operation = '+'
 
        case '?':
            l = operation[1]
            r = operation[2]
 
            sum = calculate_sum(root, int(l), int(r))
            prev_operation = '?'
            print(sum)
