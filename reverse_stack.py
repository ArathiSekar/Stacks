#Reverse a stack. If your stack initially has 1, 2, 3, 4 (4 at the top and 1 at the bottom), after reversing the order must be 4, 3, 2, 1 (4 at the bottom and 1 at the top).
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

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
        popped = self.head
        self.num_elements -= 1
        self.head = self.head.next
        return popped
    
    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
        
    def print_stack(self):
        current_node = self.head
        while(current_node):
            print(current_node.value)
            current_node = current_node.next

    def top(self):
        if self.head is None:
            return None
        return self.head.value

def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)
    
    return stack    
        
def reverse_stack(stack):
    holder_stack = Stack()
    while(not stack.is_empty()):
        i = stack.pop()
        holder_stack.push(i.value)
    
    holder_stack.print_stack()
    
   

test_case_1 = [1, 2, 3, 4]
reverse_stack(test_function(test_case_1))

test_case_2 = [1]
reverse_stack(test_function(test_case_2))     
