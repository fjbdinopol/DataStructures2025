class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):               # push() Adds an item to the top of the stack.
        self.stack.append(item)

    def pop(self):                      # pop() Removes and returns the top item from the stack (if it's not empty).
        if not self.is_empty():         
            return self.stack.pop()     # Checks if the stack is empty.
        return "Stack is empty"
    
    def is_empty(self):                 # Checks if the stack is empty.
        return len(self.stack) == 0
    
    def peek(self):                     # peek() Returns the top element without removing it.
        return self.stack[-1] if not self.is_empty() else "Stack is empty"
    

stack2 = Stack()
stack2.push("A")
stack2.push("B")
print(stack2.peek())  

# Returns B element without removing it.
