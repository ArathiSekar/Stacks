#Implement queue using stack

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        
        self.s1 = Stack()
        self.s2 = Stack()
        
    def size(self):
        
        return (self.s1.size() + self.s2.size())
        
    def enqueue(self,item):
       
        self.s1.push(item)
        
    def dequeue(self):
       
        if (not self.s2.items):
            while(self.s1.size()):
                self.s2.push(self.s1.pop())
        
        return self.s2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
