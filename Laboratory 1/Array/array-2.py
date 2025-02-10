class Array:
    def __init__(self):                         # Initializes an empty array.
        self.array = []
    
    def insert(self, value):                    # Adds a new value to the array.
        self.array.append(value)

    def delete(self, index):                    # Removes the element at a given index.
        if 0 <= index < len(self.array):        
            return self.array.poop(index)
        return "Invalid index"

arr2 = Array()
arr2.insert("Hello")
arr2.insert("World")
print(arr2.delete(1))

# prints out World because the index 1 is equal to the second element which is World
