#Implement stack using queue
class Queue:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        if(self.size()==0):
            return None
        else:
            return self.items.pop(0)

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def size(self):
        return (self.q1.size() + self.q2.size())
    
    def push(self, item):
        # moving from first queue to second queue in the exact same order
        while(self.q1.size()):
            self.q2.enqueue(self.q1.dequeue())
        
        # adding the item to the first queue, so that it is now at the beginning of the queue instead of at the end
        self.q1.enqueue(item)
        
        # moving the elements from second queue back to the first , after item
        while(self.q2.size()):
            self.q1.enqueue(self.q2.dequeue())
    
    def pop(self):
        while(self.q1.size()):
            return self.q1.dequeue()
                
                
s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.size())
print(s.pop())
print(s.pop())
