class Array:
    def __init__(self):                         # Initializes an empty array.
        self.array = []
    
    def insert(self, value):                    # Adds a new value to the array.
        self.array.append(value)

    def delete(self, index):                    # Removes the element at a given index.
        if 0 <= index < len(self.array):        
            return self.array.pop(index)
        return "Invalid index"

arr1 = Array()
arr1.insert(1)
arr1.insert(2)
print(arr1.delete(0))

# prints out 1 because the index 0 is equal to the first element which is 1
