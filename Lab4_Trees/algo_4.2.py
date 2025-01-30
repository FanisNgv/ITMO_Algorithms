from random import randint
from sys import stdin

class Node:
    def __init__(self, value=None, priority=None, left=None, right=None, index=None):
        self.value: int = value
        self.priority: int = priority
        self.left: Node = left
        self.right: Node = right
        self.index: int = index

    def split(self, root: 'Node', x0: int):
        # Если root None, то ниже мы уже не спустимся, не поделим
        if root == None:
            return None, None
        # Если x0 больше чем рут, значит он больше всех значений в левом поддереве
        # Сплиттим теперь по правой дочери рута с тем же x0
        if root.value < x0:
            a, b = self.split(root.right, x0)
            # a - это root.right, а b - это поддерево для x0
            root.right = a
            return root, b
        elif root.value >= x0:
            # делаем то же самое, но для левого поддерева, т.к. x0 меньше рута
            a, b = self.split(root.left, x0)
            # root.left равен правому разбиению поддерева, т.к. b - это та часть, которая нас не интересует
            # при разбиении, она остается для текущего корня
            root.left = b
            return a, root 

    # условие, что слева все меньше, чем справа
    def merge(self, node_1: 'Node', node_2: 'Node'):
        # если не с чем мержит, возвращаем просто одно из вершин, которое не None
        if node_1 == None:
            return node_2
        if node_2 == None:
            return node_1

        # Если приоритет первого меньше, чем второго, то его правого мержим с текущим вторым, т.к. он
        # скорее всего будет ближе ко второму ноду
        if node_1.priority < node_2.priority:
            node_1.right = self.merge(node_1.right, node_2)
            return node_1
        else:
            node_2.left = self.merge(node_1, node_2.left)
            return node_2

    def insert(self, root: 'Node', x0: int):
            # в "a" все, что меньше икса, в b больше либо равно 
            a, b = self.split(root, x0)
            # с больше либо равно икса и меньше x + 1, значит это х!
            c, d = self.split(b, x0 + 1)
            c = Node(x0, randint(100, 999), None, None)
            return self.merge(a, self.merge(c, d))

    def index_in_breadth_and_collect(self, root: 'Node'):
        index = 1
        nodes_list = []
        if root is None:
            return nodes_list

        nodes = [root]
        while nodes:
            next_level = []
            for node in nodes:
                node.index = index
                nodes_list.append(node)
                index += 1

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            nodes = next_level
        return nodes_list

    def print_in_order(self, root: 'Node'):
        nodes_list = []
        self.collect_nodes_in_order(root, nodes_list)
        output_list = [None] * len(nodes_list)

        for node in nodes_list:
            left_index = node.left.index if node.left else -1
            right_index = node.right.index if node.right else -1
            # добавляем в соответствующий индекс в списке, чтобы отобразить своевременно
            output_list[node.index - 1] = str(node.value) + " " + str(left_index) + " " + str(right_index)
        
        for entry in output_list:
            print(entry)

num_of_nodes = int(input())
value_of_nodes = list(map(int, input().split()))

root = Node(value_of_nodes[0], randint(100, 999), None, None)
for i in range(1, num_of_nodes):
    root = root.insert(root, value_of_nodes[i])

root.index_in_breadth(root)

print(num_of_nodes)
root.print_in_order(root)
print(1)


'''# класс узла
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.index = None

# класс дерева
class BST:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, None, None)
        else:
            self.insert_recursive(self.root, value)

    # вставляем рекурсивно просто по свойству дерева (идем влево-вправо, ориентируясь на знак)
    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value, None, None)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right, value)


    def index_nodes(self):
        queue = [self.root]
        index = 1

        # идем индексировать в ширину
        while queue:
            node = queue.pop(0)
            node.index = index
            self.nodes.append(node)
            index += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def print_tree(self):

        for node in self.nodes:
            left_index = node.left.index if node.left else -1
            right_index = node.right.index if node.right else -1
            print(node.value, left_index, right_index)



n = int(input())
values = [int(x) for x in input().split()]

bst = BST()
for value in values:
    bst.insert(value)

bst.index_nodes()

print(n)
bst.print_tree()
print(bst.root.index)'''