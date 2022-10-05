Our queue will need to have the following functionality:

#enqueue - adds data to the back of the queue
#dequeue - removes data from the front of the queue
#front - returns the element at the front of the queue
#size - returns the number of elements present in the queue
#is_empty - returns True if there are no elements in the queue, and False otherwise
#_handle_full_capacity - increases the capacity of the array, for cases in which the queue would otherwise overflow
#Also, if the queue is empty, dequeue and front operations should return None.

class Queue:
    def __init__(self, initial_size=5):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.num_elements = 0
        

    def enqueue(self,value):
        if(len(self.arr) == self.num_elements):
            self.handle_full_capacity()
            
        self.arr[self.next_index] = value
        self.next_index = (self.next_index + 1)% len(self.arr)
        self.num_elements += 1
        if (self.front_index == -1):
            self.front_index = 0
    
    
    def handle_full_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2*len(old_arr))]
        index = 0
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            print(i)
            index += 1
        
        # case: when front-index is befire of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            print(i)
            index += 1

        
        self.front_index = 0
        self.next_index = index
        
    def dequeue(self):
        if (self.is_empty()):
            self.next_index = 0
            self.front_index = -1
            return None
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.num_elements -= 1
        return value
    
    def is_empty(self):
        return (self.size == 0)
    
    def front(self):
        if (self.is_empty()):
            return None
        return (self.arr[self.front_index])
        
    def size(self):
        return self.num_elements
    
    

q = Queue()
print(q.arr)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.dequeue()
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
print(q.arr)
