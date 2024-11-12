""" 
Delete node from singly-linked list
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_and_print(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")

def delete_node(head, node):
    if head == node:
        return head.next

    current_node = head
    while current_node.next and current_node.next != node:
        current_node = current_node.next

    if current_node.next is None:
        return head

    current_node.next = current_node.next.next
    return head

a = Node(20)
b = Node(30)
c = Node(40)
d = Node(10)
e = Node(70)

a.next = b
b.next = c
c.next = d
d.next = e

# All nodes
traverse_and_print(a)

# Deleting node c
a = delete_node(a, c)

# Final
traverse_and_print(a)