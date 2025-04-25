# Linked List 

The Linked list in python are the data storage structures where fundamental `nodes` are present which store the data. These datastructures are not contiguous unlike the arrays! The Nodes therefore need to point to another memory location in order to access the data.

The following is the general Node structure:
- Node contains the data
- Node contains the pointer which points to the next Node.

For this purpose we make use of the Class creation for serving the purpose of LinkedLists

```python

# Singly LinkedList
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

    # Just the way of printing the data
    # def __str__(self):
    #     return str(self.data)
Head = Node(2)
A = Node(23)
B = Node(3)

Head.next = A
A.next = B

# Doubly LL
class DoublyNode:
    
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = None
        self.prev = None

    __str__:
        print(f"The previous node is {self.prev} and next is {prev.next}")


N1 = DoublyNode(1)
N2 = DoublyNode(2)
N3 = DoublyNode(3)

N1.prev = None
N1.next = N2
N2.prev = N1
N2.next = N3
N3.prev = N2
N3.next = None 
```

> The head is used for denoting the start of the LinkedList


Doubly LinkedList is similar to the Singly but this will also have the pointer to previous Node. Thereby since the Head was the first, in the Doubly LL we have the tail denoting the last Node of the LL





## Traversal Head

For the purpose of traversal we will need to create variable that can be traversed without affecting the current status of the Nodes

```python
curr = Head # Note that we are not creating a new Object, we are creating variable for pointing out head

l = []
while curr:  #OR while(curr != None): 
    l.append(str(curr.data))
    curr = curr.next

print('->'.join(l))
```



## Searching 


```python
def search(head, val):
    curr = Head
    while curr:
        if curr.data == val:
            return True
        curr = curr.next
    return False

```