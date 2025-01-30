# Есть у нас операция вставки, передается позиция и некоторое положительное число
# Если ячейка занята, то смещаем то, что там лежим в положение + 1
# Добавление элементов идет 1, 2, 3, ... и так далее

from random import randint
import random
import sys

class Node:
    def __init__(self, priority=None, left=None, right=None, size=1, flag=0, data=0, index_right_zero = -1, key = 0):
        self.priority: int = priority
        self.left: Node = left
        self.right: Node = right
        self.size: int = size
        self.flag: int = flag
        self.data: int = data
        self.index_right_zero: int = index_right_zero
        self.key: int = key


def remember_all(root: Node, k: int):
    if root is None:
        return
    root.key = k + size_of(root.left) + 1
    remember_all(root.left, k)
    remember_all(root.right, k + size_of(root.left) + 1)


def size_of(v: Node) -> int:
    return v.size if v is not None else 0

def get_right_zero(v: Node) -> int:
    return v.index_right_zero if v is not None else -1

def data_of(v: Node) -> int:
    return v.data if v is not None else 0

def recalc(v: Node):
    global tree
    if v:
        v.size = size_of(v.left) + size_of(v.right) + 1
        # remember_all(tree, 0)

        # if v.data == 0:
        #     v.index_right_zero = v.key
        #     # тут разобраться, get_node 0 нотация или 1
        # else:
        #     # тут неправильно, т.к. райт может быть наном, хотя по списку элемент есть 
        #     v.index_right_zero = get_right_zero(get_node(tree, v.key + 1)[0])
        #     pass

    return v



def merge(root1: Node, root2: Node) -> Node:
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    if root1.priority < root2.priority:
        root1.right = merge(root1.right, root2)
        return recalc(root1)
    else:
        root2.left = merge(root1, root2.left)
        return recalc(root2)

def split(root: Node, x0: int, k: int):
    if root is None:
        return None, None

    if (k + size_of(root.left)) < x0:
        (root.right, other) = split(root.right, x0, k + size_of(root.left) + 1)
        return recalc(root), other
    else:
        (other, root.left) = split(root.left, x0, k)
        return other, recalc(root)


def insert(root: Node, x0: int, data: int, x_old: int) -> Node:
    global max_index

    # Если текущий узел пустой, то можно вставить новый элемент
    if root is None:
        # Вставляем новый элемент в пустое место
        node = Node(priority=randint(1, 2**31 - 1), data=data)
        
        max_index += 1

        return node

    # Получаем текущее значение по позиции
    current_value, root = get(root, x0)

    if current_value == 0:
        # Если текущая ячейка свободна, просто вставляем новый элемент
        if x0 + 1 + x_old > max_index:
            max_index = x0 + 1 + x_old

        # Разделяем дерево по индексу x0, потом вставляем новый узел
        a, b = split(root, x0, 0)
        (c, b) = split(b, 1, 0)

        c = Node(priority=randint(1, 2**31 - 1), data=data)
        
        # Объединяем разделенные деревья с новым элементом
        return merge(a, merge(c, b))
    else:
        # Если на месте, куда хотим вставить, уже есть число, то мы должны
        # заменить его новым числом и сдвигать оставшиеся элементы рекурсивно
        (temp1, temp2) = split(root, x0, 0)
        number = get(temp2, 0)[0]
        (c, temp2) = split(temp2, 1, 0)
        
        # Вставляем новый элемент на место старого
        c = Node(priority=randint(1, 2**31 - 1), data=data)
        root = merge(temp1, merge(c, temp2))

        # Сдвигаем оставшуюся часть и рекурсивно вставляем сдвинутый элемент
        (a, b) = split(root, x0 + 1, 0)
        b = insert(b, 0, number, x_old + x0 + 1)

        # Объединяем дерево после вставки
        return merge(a, b)



def insert_default(root: Node, x0: int, data: int, shifting: bool = True) -> Node:
    (a, b) = split(root, x0, 0)
    if not shifting:
        (c, b) = split(b, 1, 0)
    c = Node(priority=randint(1, 2**31 - 1), data=data)
    return merge(a, merge(c, b))

def get(root: Node, x0: int):
    (a, b) = split(root, x0, 0)
    (c, d) = split(b, 1, 0)
    return data_of(c), merge(a, merge(c, d))

def get_node(root: Node, x0: int):
    (a, b) = split(root, x0, 0)
    (c, d) = split(b, 1, 0)
    return c, merge(a, merge(c, d))


def print_tree(node: Node):
    global max_index

    if node is None or max_index <= 0:
        return
    print_tree(node.left)
    if max_index > 0:
        # sys.stdout.write(f"{node.data}(index: {node.key} l_null: {node.index_right_zero}) ")
        sys.stdout.write(f"{node.data} ")
        max_index -= 1
    print_tree(node.right)


tree: Node = None

input_data = [int(x) for x in sys.stdin.readline().split()]

operations_count = input_data[0]
max_position = input_data[1]

input_data = [int(x) for x in sys.stdin.readline().split()]

insert_number = 1
#random.seed(42)

for i in range(max_position):
    tree = insert_default(tree, i, 0)
    insert_number += 1

insert_number = 1

max_index = 1

for i in range(operations_count):
    tree = insert(tree, input_data[i] - 1, insert_number, 0)
    insert_number += 1

print(max_index)
print_tree(tree)
