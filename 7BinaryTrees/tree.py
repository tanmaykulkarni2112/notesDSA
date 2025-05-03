class Treenode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
    
    def __str__(self):
        return str(self.val)

A = Treenode(1)
B = Treenode(2)
C = Treenode(3)
D = Treenode(4)
E = Treenode(5)
F = Treenode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A)

# Recursive algorithm for DFS
def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)
    
def in_order(node):
    if not node: 
        return
    in_order(node.left)
    print(node)
    in_order(node.right)
print("INorder")
in_order(A)


def post_order(node):
    if not node:
        return 
    post_order(node.left)
    post_order(node.right)
    print(node)
print("POSTORDER")

post_order(A)

# BFS
print("-------BFS-------")
from collections import deque

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left : q.append(node.left)
        if node.right : q.append(node.right)

bfs(A)

## Checking for value in df

def checkdfs(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    return checkdfs(node.left, target) or checkdfs(node.right, target)

isfound = checkdfs(A,3)
print(isfound)