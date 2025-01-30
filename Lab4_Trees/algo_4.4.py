from random import randint
from sys import stdin

class Node:
    def __init__(self, value=None, priority=None, left=None, right=None):
        self.value: int = value
        self.priority: int = priority
        self.left: Node = left
        self.right: Node = right

def split(root: Node, x0: int):
    # Если root None, то ниже мы уже не спустимся, не поделим
    if root == None:
        return None, None
    # Если x0 больше чем рут, значит он больше всех значений в левом поддереве
    # Сплиттим теперь по правой дочери рута с тем же x0
    if root.value < x0:
        a, b = split(root.right, x0)
        # a - это root.right, а b - это поддерево для x0
        root.right = a
        return root, b
    elif root.value >= x0:
        # делаем то же самое, но для левого поддерева, т.к. x0 меньше рута
        a, b = split(root.left, x0)
        # root.left равен правому разбиению поддерева, т.к. b - это та часть, которая нас не интересует
        # при разбиении, она остается для текущего корня
        root.left = b
        return a, root 

# условие, что слева все меньше, чем справа
def merge(node_1: Node, node_2: Node):
    # если не с чем мержит, возвращаем просто одно из вершин, которое не None
    if node_1 == None:
        return node_2
    if node_2 == None:
        return node_1

    # Если приоритет первого меньше, чем второго, то его правого мержим с текущим вторым, т.к. он
    # скорее всего будет ближе ко второму ноду
    if node_1.priority < node_2.priority:
        node_1.right = merge(node_1.right, node_2)
        return node_1
    else:
        node_2.left = merge(node_1, node_2.left)
        return node_2

def insert(root: Node, x0: int):
        # в "a" все, что меньше икса, в b больше либо равно 
        a, b = split(root, x0)
        # с больше либо равно икса и меньше x + 1, значит это х!
        c, d = split(b, x0 + 1)
        c = Node(x0, randint(100, 999), None, None)
        return merge(a, merge(c, d))

def delete(root: 'Node', x0: int):
    # в "a" все, что меньше икса, в b больше либо равно 
    a, b = split(root, x0)
    # с больше либо равно икса и меньше x + 1, значит это х!
    c, d = split(b, x0 + 1)
    c = None
    return merge(a, d)

def exists(root: 'Node', x0: int):
    exists = False
    # в "a" все, что меньше икса, в b больше либо равно 
    a, b = split(root, x0)
    # с больше либо равно икса и меньше x + 1, значит это х!
    c, d = split(b, x0 + 1)
    if c is not None:
        exists = True
    root = merge(a, merge(c, d))
    return exists

def next(root: Node, x0: int):
    a, b = split(root, x0 + 1)

    if b is None:
        return None
    elif b.value == x0:
        b = b.right

    nearest_greater = find_min(b)
    
    root = merge(a, b)
    
    return nearest_greater

def find_min(root: Node):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root.value

def prev(root: Node, x0: int):
    a, b = split(root, x0)
    if a is None:
        return None
    
    nearest_less = find_max(a)
    
    root = merge(a, b)

    return nearest_less
    
def find_max(root: Node):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root.value


root = None

for operation in stdin:
    operation = operation.split()
    if operation[0] == 'insert':
        if root == None:
            root = Node(int(operation[1]),randint(100, 999), None, None)
        else:
            root = insert(root, int(operation[1]))

    elif operation[0] == 'delete':
        root = delete(root, int(operation[1]))

    elif operation[0] == 'exists':
        isExists = exists(root, int(operation[1]))
        if isExists:
            print('true')
        else:
            print('false')

    elif operation[0] == 'next':
        result = next(root, int(operation[1]))
        if result is not None:
            print(result)
        else:
            print('none')

    elif operation[0] == 'prev':
        result = prev(root, int(operation[1]))
        if result is not None:
            print(result)
        else:
            print('none')
