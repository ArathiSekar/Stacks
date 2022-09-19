#Implement a Stack using Linkedlist
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0
    
    
    def push(self,value):
        if (self.head is None):
            self.head = Node(value)
        
        else:
            #Add new element to head of stack to make push & pop easier 
            current_node = Node(value)
            current_node.next = self.head
            self.head = current_node
        
        self.num_elements +=1


    def size(self):
        return self.num_elements

    
    def isEmpty(self):
        return (self.num_elements==0)
    
    
    def pop(self):
        if(self.head is None):
            return None
        popped = self.head
        self.num_elements -=1
        self.head = self.head.next
        return popped
    
    
    def print_stack(self):
        current_node = self.head
        while(current_node):
            print(current_node.value)
            current_node = current_node.next
        
s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.size())
print(s.isEmpty())

#s.print_stack()

s.pop()

s.print_stack()

 

            
