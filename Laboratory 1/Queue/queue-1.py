from collections import deque           # double-ended queue for fast insertions and deletions from both ends

class Queue:
    def __init__(self):                 # Initializes an empty queue.
        self.queue = deque()
    
    def enqueue(self, item):            # Adds an item to the queue.
        self.queue.append(item)
    
    def dequeue(self):                  # Removes and returns the first item.
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"
    
    def is_empty(self):                 # Checks if the queue is empty.
        return len(self.queue) == 0

queue1 = Queue()
queue1.enqueue(5)
queue1.enqueue(15)
print(queue1.dequeue())  

# prints out 5 since its the first element in the queue
