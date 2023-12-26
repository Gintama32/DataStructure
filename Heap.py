#implementation of heap tree
class Heap:
    #initializing an empty array to store our data
    def __init__(self):
        self.heap = []
    #returns first element of array as root node
    def root_node(self):
        return self.heap[0]
    #returns last element of array as last node
    def last_node(self):
        return self.heap[len(self.heap)-1]
    #this is just to iterate over the tree by setting range with this indx later in this code.
    def last_node_idx(self):
        return len(self.heap)-1
    #insert method of our array, takes value and inserts it into right place by comparing the new value with its parent value and exchanging places if necessary.
    def insert(self,val):
        self.heap.append(val)
        new_node_idx = len(self.heap)-1
    #need make sure that our new node is not root node because we dont want to compare root node with its non-existent parent which could break the program.
    #the other is just checking the values of two nodes between new node and its parent node
        while new_node_idx > 0 and self.heap[new_node_idx]>self.heap[self.parent_idx(new_node_idx)]:
            self.heap[self.parent_idx(new_node_idx)],self.heap[new_node_idx] = self.heap[new_node_idx],self.heap[self.parent_idx(new_node_idx)]
            new_node_idx = self.parent_idx(new_node_idx)
    def parent_idx(self,child_idx):
        return ((child_idx-1)//2)
    
    def left_idx(self,parent):
        return ((parent*2)+1)
    
    def right_idx(self,parent):
        return ((parent*2)+2)
    
    def left_child(self,parent):
        return self.heap[((parent*2)+1)]
    
    def right_child(self,parent):
        return self.heap[((parent*2)+2)]
    
heap = Heap()
heap.insert(1)
heap.insert(10)
heap.insert(9)
heap.insert(8)
print("This is root node")
print(heap.root_node())
print("Lets check out the left child indx of 1:")
print(heap.left_child(1))
print("This should also be the last node of our heap tree:")
print(heap.last_node())
#representing the heap tree in array form to make clarification on indexing of nodes or items in the tree
#start with root node as first element in an empty array
array =[heap.root_node()]
#iterate to put the left and right child in the right place
for i in range((heap.last_node_idx())+1):
#if left child or right child is last node, we dont want to insert their left or right child since it does not have one. So, we break out of the loop but append the last node before breaking 
#out of it to make sure that we append our last node 
    if heap.left_child(i)==heap.last_node() or heap.right_child(i)==heap.last_node():
        array.append(heap.last_node())
        break
#if left child is there of a ith parent element then insert it into correct place
    if heap.left_child(i) != None:
        array.insert(heap.left_idx(i),heap.left_child(i))
    if heap.right_child(i) != None:
#if right child is there of ith parent element then insert it into correct place
        array.insert(heap.right_idx(i),heap.right_child(i))
print(array)
    

    