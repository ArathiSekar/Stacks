# Reverse a Queue using a stack

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
        self.num_elements +=1
    
    def dequeue(self):
        if (self.head is None):
            return None
        
        popped = self.head.value
        self.head = self.head.next 
        self.num_elements -=1
        return popped
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements==0


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self,value):
        if(self.head is None):
            self.head = Node(value)
        else:
            current_node = Node(value)
            current_node.next = self.head
            self.head = current_node
        self.num_elements +=1
    
    def pop(self):
        if(self.head is None):
            return None
        popped = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return popped    
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return (self.num_elements==0)
        
def reverse(q):
    s = Stack()
    while(not q.is_empty()):
        s.push(q.dequeue())
    
    while(not s.is_empty()):
        q.enqueue(s.pop())
    
    print_ds(q)
    
def print_ds(ds):
    current_node = ds.head
    while(current_node):
        print(current_node.value)
        current_node = current_node.next
    
def test_function(test_case):
    q = Queue()
    for num in test_case:
        q.enqueue(num)    
    return q  
        
test_case_1 = [1, 2, 3, 4]
reverse(test_function(test_case_1))
        
