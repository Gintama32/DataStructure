#implementing queue data structure using python's list
class Queue:
    def __init__(self):
        self.queue = []
#adding item in the queue
    def enqueue(self,item):
            self.queue.append(item)
#removing item from the queue    
    def dequeue(self):
         if len(self.queue)==0:
              print("Queue is empty!")
         else :
              return self.queue.pop(0)
#reading the first item in the queue
    def read(self):
         if len(self.queue)==0:
               print("Nothing to read, queue is empty!")
         else:
              print(self.queue[0])
#displaying the items stored in the queue
    def display(self):
         for i in range(len(self.queue)):
              print(self.queue[i])
#initializing our Queue structure
my_queue = Queue()
#adding items in the queue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
#displaying the queue to see the queue after adding items
my_queue.display()
#reading the first item of the queue
print("The first in queue is ",end="-> ")
my_queue.read() #output -> 1
#removing item from first in queue, should return 1
print("Dequeued this item ", end="-> ")
print(my_queue.dequeue()) #output is 1
#displaying the queue again to check if the item is successfully dequeued..
print("Our queue after removing first item")
my_queue.display()
#always adds from the last of the queue
my_queue.enqueue(1)
#checking again to see if 1 is added at last or not
print("#1 is added to last of the queue")
my_queue.display()

    