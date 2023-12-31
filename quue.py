class Node:
    def __init__(self,data,next_node=None,prev_node=None):
        self.data = data
        self.next_node= next_node
        self.prev_node = prev_node
class Double_LnkedLst:
    def __init__(self,first_node=None,last_node=None):
        self.first_node = first_node
        self.last_node = last_node
    
    def insert_at_end(self,item):
        new_node = Node(item)
        if self.first_node is None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.prev_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node
    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node
    def display(self):
        current_node = self.first_node
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
    def reverse(self):
        current_node =self.last_node
        while current_node:
            print(current_node.data)
            current_node = current_node.prev_node   
    
class Queue:
    def __init__(self):
        self.queue = Double_LnkedLst()
    def enqueue(self,item):
        self.queue.insert_at_end(item)
    def dequeue(self):
        removed_node= self.queue.remove_from_front()
        return removed_node.data
    def read(self):
        if self.queue.first_node is None:
            return None
        else:
            return self.queue.first_node.data
        
    def displays(self):
        return self.queue.display()
    def reversed(self):
        return self.queue.reverse()
new_queue = Queue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
print("#All the elements in the queue:")
new_queue.displays()
print("#All the elements in the queue in reverse order:")
new_queue.reversed()
print("#Should get first item with read function ", end="-> ")
print(new_queue.read())
print("#Should remove first item in the queue with dequeue ", end="-> ")
print(new_queue.dequeue())
print("#We should get all items except first item:")
new_queue.displays()