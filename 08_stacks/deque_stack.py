""" 
Deque stack
"""

from collections import deque

class DequeStack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

if __name__ == "__main__":
    s = DequeStack()

    s.push(5)
    s.push(9)
    s.push(34)
    s.push(78)
    s.push(12)
    print(s.size())