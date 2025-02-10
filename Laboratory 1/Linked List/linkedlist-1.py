class Node:
    def __init__(self, data):
        self.data = data    # Stores the value
        self.next = None    # Pointer to the next node (default is None)

class LinkedList:
    def __init__(self):
        self.head = None    # Initializes an empty linked list

    def insert(self, data): # Creates a new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node    # If empty, make it the head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next    # Traverse to the last node
            temp.next = new_node    # Add the new node at the end
    
    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)    # Collects all values
            temp = temp.next            # Moves to the next node
        return result   
    
ll1 = LinkedList()
ll1.insert(100)
ll1.insert(200)
print(ll1.display())

# Therefore the output is: [100, 200]