""" 
Class example of queue
"""

class Queue:
    def __init__(self):
        self.data = []
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def getSize(self):
        return len(self.data)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.data[0]
    
    def enqueue(self, element):
        self.data.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.data.pop(0)


q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print("Queue: ", q.data)
print("Dequeue: ", q.dequeue())
print("Peek: ", q.peek())
print("isEmpty: ", q.isEmpty())
print("Size: ", q.getSize())