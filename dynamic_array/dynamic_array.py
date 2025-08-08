class DynamicArray:
    """Implementation of dynamic array
    """

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

    def contains(self, x):
        """Method to check whether an item is in the array

        1. Loop through each item in the array
        2. If there is an item equal to x, return True
        3. If after looping all items and no item equal to x found, return False
        """
        for i in range(self.size):
            if self.arr[i] == x:
                return True
        return False

    def insert(self, i, x):
        """Method to insert item x at index i

        1. Check if the index is equal to the size, then we just need to append
        2. Check if the size is equal to the capacity. If yes, we need to increase the size before inserting
        3. Loop backwards from the last index of the array and assign the right index with its left one (shift everything to the right)
        4. Assign the value x at index i
        """
        if i == self.size:
            self.append(x)
            return

        if self.size == self.capacity:
            self.resize(2 * self.capacity)

        for j in range(self.size - 1, i - 1, -1):
            self.arr[j + 1] = self.arr[j]

        self.arr[i] = x
        self.size += 1

    def remove(self, x):
        """Method to remove the first instance of item x"""
        for i in range(self.size):
            if self.arr[i] == x:
                self.pop(i)
                return i
        return -1

    def pop(self, i):
        """Method to remove the item at index i
        (shift everything to the left after removing the item)
        """
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        x = self.arr[i]

        for j in range(self.size):
            self.arr[j] = self.arr[j + 1]

        self.size -= 1

        return x
