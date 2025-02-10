class Stack:
    def __init__(self):                 # Initializes an empty stack.
        self.stack = []

    def push(self, item):               # push() Adds an item to the top of the stack.
        self.stack.append(item)

    def pop(self):                      # pop() Removes and returns the top item from the stack (if it's not empty).
        if not self.is_empty():         
            return self.stack.pop()     # Checks if the stack is empty.
        return "Stack is empty"
    
    def is_empty(self):                 # Checks if the stack is empty.
        return len(self.stack) == 0
    
stack1 = Stack()
stack1.push(10)
stack1.push(20)
print(stack1.pop())

# Removes the 20 and returns it
