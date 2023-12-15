# Node class with data and pointer to next node as parameters
class Node:
    def __init__(self, data, ptr=None):
        self.data = data
        self.ptr = ptr
# linked list class
class Lnked_List:
    def __init__(self):
        self.first_node = None

# implementation of insertion method on linked list based on the given index and given node
    def insert(self,new_node,index = 0):
        if index == 0:
            new_node.ptr = self.first_node
            self.first_node = new_node
            return
        current_node = self.first_node
        position =0
        while current_node:
            if position==index-1:
                new_node.ptr = current_node.ptr
                current_node.ptr= new_node
                return
            current_node= current_node.ptr
            position += 1
        current_node.ptr = new_node
 # implentation of read method that reads data from particular index given by the user
    def read(self, index):
        current_node= self.first_node
        if index == 0:
            return current_node.data
        position =0
        while current_node:
                if position == index:
                    return current_node.data
                current_node = current_node.ptr
                position +=1
        return False
    # implementation of search method that searches for particular item and returns false if not found in the list
    def search(self, item):
        current_node = self.first_node
        position =0
        while current_node:
            if current_node.data == item:
                return position
            position += 1
            current_node = current_node.ptr
        return False
    # implements delete method in the linked list that deletes the node of given index. Returns a message if the index is out of list.
    def delete(self, index):
        current_node = self.first_node

        if index == 0:
            if current_node:
                self.first_node = current_node.ptr
                return
            else:
                return "List is empty"

        position = 0
        while current_node:
            if position == index - 1:
                if current_node.ptr:
                    current_node.ptr = current_node.ptr.ptr
                    return
                else:
                    return "Index out of list"
            position += 1
            current_node = current_node.ptr

        return "Index out of list"
# simple implementation of a display method to display or pritnt out the contents of the linked list
    def display(self):
        current_node = self.first_node
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.ptr
        print()



# Creating a linked list...
lnk_list = Lnked_List()
# building nodes...
node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
#inserting nodes...
lnk_list.insert(node1)
lnk_list.insert(node2,1)
lnk_list.insert(node3,2)
lnk_list.insert(node4,3)
# Searching for an item in the linked list
print(lnk_list.search("c")) #output should be 2
# reading whats in the index 0 of the linked list
print(lnk_list.read(0)) #output should be a
#testing out delete method...
print("Initial linked list before deletion:")
lnk_list.display() #output should be (a b c d)
lnk_list.delete(1)
print("Linked List after deletion")
lnk_list.display() #output should be (a c d)
