#Reverse Polish notation.Create a function that does the following:Given a postfix expression as input, evaluate and return the correct final answer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        popped = self.head
        self.num_elements -=1
        self.head = self.head.next
        return popped

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def print_stack(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
    
def evaluate_post_fix(input_list):
    s = Stack()
    for i in input_list:
        if (i == "*"):
            second = s.pop()
            first = s.pop()
            output = first.data * second.data
            s.push(output)
        elif (i=="+"):
            second = s.pop()
            first = s.pop()
            output = first.data + second.data
            s.push(output)
        elif (i=="-"):
            second = s.pop()
            first = s.pop()
            output = first.data - second.data
            s.push(output)
        elif (i=='/'):
            second = s.pop()
            first = s.pop()
            output = int(first.data/second.data)
            s.push(output)
        else:
            s.push(int(i))
    
    
        s.print_stack()
        print("\n")
        
test_case_1 = ["3", "1", "+", "4", "*"]
#output = [(3 + 1) * 4 = 16]
#evaluate_post_fix(test_case_1)

test_case_2 = ["4", "13", "5", "/", "+"]
#evaluate_post_fix(test_case_2)

test_case_3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
evaluate_post_fix(test_case_3)
