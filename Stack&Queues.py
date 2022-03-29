## Stack Class Implementation
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def remove(self):
        self.items.pop()

    def printStack(self):
        print("Stack = ", self.items)




## Queue Class Implementation
class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def remove(self):
        if len(self.items) != 0:
            self.items.pop(0)
    
    def printQueue(self):
        print("Queue = ", self.items)





