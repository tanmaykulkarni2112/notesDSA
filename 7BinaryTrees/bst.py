class treenode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

A = treenode(10)
B = treenode(3)
C = treenode(11)
D = treenode(2)
E = treenode(13)
F = treenode(5)

A.left = B
B.left = D
A.right = C
C.right = E
B.right = F

def printer(node):
    if not node:
        return
    print(node)
    printer(node.left)
    printer(node.right)

printer(A)

def search(node, target):
    if not node:
        return False
    if node.value == target:
        return True
    if target < node.value: return search(node.left, target)
    if target > node.value: return search(node.right, target)
print(search(A, 13))


#       10

#    3      11

#  2   5       13