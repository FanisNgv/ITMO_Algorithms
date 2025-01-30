from random import randint
import sys

max_int = sys.maxsize
min_int = -sys.maxsize - 1

class Vertex:
    def __init__(self, value = None, left = None, right = None):
        self.value: int = value
        self.left: Vertex = left
        self.right: Vertex = right


def maxValue(vertex: Vertex):
    if (vertex == None):
        return min_int
    elif (vertex.left != None and vertex.right != None):
        return max(vertex.value, vertex.left.value, vertex.right.value)
    elif (vertex.left != None and vertex.right == None):
        return max(vertex.value, vertex.left.value)
    elif (vertex.left == None and vertex.right != None):
        return max(vertex.value, vertex.right.value)
    else:
        return vertex.value

def minValue(vertex: Vertex):
    if (vertex == None):
        return max_int
    elif (vertex.left != None and vertex.right != None):
        return min(vertex.value, vertex.left.value, vertex.right.value)
    elif (vertex.left != None and vertex.right == None):
        return min(vertex.value, vertex.left.value)
    elif (vertex.left == None and vertex.right != None):
        return min(vertex.value, vertex.right.value)
    else:
        return vertex.value
    
def isBinarySearchTree(vertex: Vertex):
    if (vertex == None):
        return True

    if (vertex.left != None and maxValue(vertex.left) >= vertex.value):
        return False

    if (vertex.right != None and minValue(vertex.right) <= vertex.value):
        return False

    # Вернет True, только если оба вызова функций вернут True
    return isBinarySearchTree(vertex.left) and isBinarySearchTree(vertex.right)

def build_tree(vertexes, root_index):
    nodes = [Vertex(vertex[0]) for vertex in vertexes]

    for i, vertex in enumerate(vertexes):
        left_index = vertex[1]
        right_index = vertex[2]

        if left_index != -1:
            nodes[i].left = nodes[left_index - 1]

        if right_index != -1:
            nodes[i].right = nodes[right_index - 1]
    
    return nodes[root_index]

 

num_of_vertexes = int(input())
vertexes = []

for i in range(num_of_vertexes):
    cur_node = [int(x) for x in input().split()]
    vertexes.append(cur_node)

root_index = int(input()) - 1

root_vertex = build_tree(vertexes, root_index)

if (isBinarySearchTree(root_vertex)):
    print("YES")
else:
    print("NO")

