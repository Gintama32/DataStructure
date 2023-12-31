#implementing Stack data structure using list of python
class Stack:
    # initializing stack with python list
    def __init__(self):
        self.stack = []
    #pushes item at the end
    def push(self, item):
        self.stack.append(item)
    #retrives last item or top of stack
    def pop(self):
        return self.stack.pop(len(self.stack)-1)
    #looks whats on the top of stack
    def read(self):
        return self.stack[len(self.stack)-1]
    #display the whole stack items
    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i])
#initializing Stack class with an instance, my_stack
my_stack = Stack()
#pushing items in the stack...
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push('a')
my_stack.push('b')
my_stack.display()
#reading whats on the top of stack or the end of the stack
print("Top of the stack", end=" -> ")
print(my_stack.read()) #output is b
#removing top of the stack, should give b as it is on the top of stack as we have seen using read()
print("This is the popped item", end=" -> ")
print(my_stack.pop()) #output is b
#since we popped the top of the stack, we should no longer have b in the list now. Lets check using display()
my_stack.display()



