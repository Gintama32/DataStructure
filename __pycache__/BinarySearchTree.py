class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right= None
class BST:
    def __init__(self):
        self.root = None
     
    def insert(self, value):
        self.root = self.helper_insert(self.root,value)
    def helper_insert(self,root,value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self.helper_insert(root.left,value)
        else:
            root.right = self.helper_insert(root.right,value)
        return root
    def makeTree(self,array):
        for item in array:
            self.insert(item)
    def search(self,val):
        return self.search_helper(self.root,val)
    def search_helper(self,root,val):
        if root is None or root.value == val:
            return root is not None
        if val< root.value:
            return self.search_helper(root.left,val)
        else:
            return self.search_helper(root.right,val)
    def delete(self,val):
        self.delete_helper(self.root,val)
    def delete_helper(self,root,val):
        if root is None:
            return None
        elif val<root.value:
            root.left = self.delete_helper(root.left, val)
        elif val>root.value:
            root.right = self.delete_helper(root.right,val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left 
                root = None
                return temp
            temp = self.successor(root.right)
            root.value= temp.value
            root.right = self.delete_helper(root.right,temp.value)
        return root
    def successor(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current
bst = BST()
arr = [3,5,2,6,7,1]
for item in arr:
    bst.insert(item)
print(bst.search(1))
bst.delete(1)
print(bst.search(1))



