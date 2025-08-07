class DynamicArray:
    """Implementation of dynamic array"""

    def __init__(self):
        """Initialize dynamic array's attributes

        Attributes:
            - capacity (int): can be any integer that represents the initial capacity of the array
            - size (int): the initial size of the array
            - arr (list): the initial array with the size equal to its initial capacity

        Returns: None
        """
        self.capacity = 1
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        """Method to add an item to the end of the array

        1. Check if the current size has reached the capacity
        2. If yes, resize the array to be double its initial capacity
        3. If not, then assign the item x to the last index of the initial array
        4. Then, increment the size by 1
        """
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.arr[self.size] = x
        self.size += 1

    def resize(self, new_capacity):
        """Method to resize the initial array when the size exceeds the capacity

        1. Create a new array with a new capacity (doubles the size of the initial one)
        2. Loop through all items in the initial array and copy those to be the first half of the new array
        3. Assign the array to be the new array
        4. Assign the capacity to be the new capacity
        """
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def get(self, i):
        """Method to get an item at index i of the array"""
        if i < 0 or i > self.size:
            raise IndexError("Index out of bounds")
        return self.arr[i]

    def set(self, i, x):
        """Method to set an item at index i to be x value"""
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        self.arr[i] = x

    def size(self, arr):
        """Method to return the size (length) of the array"""
        return self.size

    def pop_back(self):
        """Method to remove the last item of the array

        1. Check if the array is non-empty
        2. Assign the variable val to the last item of the array
        3. Reassign the last item of the array to be None
        4. Decrease the size by 1 (because we remove one item)
        5. Return val
        """
        if self.size == 0:
            raise IndexError("Array is empty")

        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val
