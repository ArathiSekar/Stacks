#Implement Queue using Linkedlist

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    
    def enqueue(self,value):
        if(self.head is None):
            self.head = Node(value)
            self.tail = self.head
        
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
    
        self.num_elements += 1
    
    def dequeue(self):
        if(self.head is None):
            return None
        popped = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return popped
            
    def size(self):
        return (self.num_elements)
    
    def is_empty(self):
        return (self.num_elements == 0)

q = Queue()
print(q.is_empty())
