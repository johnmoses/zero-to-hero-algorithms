"""
Linked Lists
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Instantiate Node
a = Node(20)
b = Node(30)
c = Node(40)

# Traverse and print
print(a.data)

a.next = b
b.next = c

print(a.next.data)
print(a.next.next.data)
