import ctypes

class MyArray:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._data = self.create_array(self._capacity)

    def create_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def append(self, value):
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove_by_value(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                for j in range(i, self._size - 1):
                    self._data[j] = self._data[j + 1]
                self._data[self._size - 1] = None
                self._size -= 1
                return
        raise ValueError("Value not found!")

    def remove_by_index(self, index):
        if index < self._size:
            for i in range(index, self._size - 1):
                self._data[i] = self._data[i + 1]
            self._data[self._size - 1] = None
            self._size -= 1
        else:
            print("Out of index!")

    def display(self):
        print("Capacity:", self._capacity)
        print("Element in array:", self._size)
        for i in range(self._size):
            print(" ", self._data[i])

    def search(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                return True
        return False

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        self._data[index] = value

    def __len__(self):
        return self._size

arr = MyArray()
arr.append(1)
arr.append(2)
arr.append(3)
arr.display()
arr.append(4)
arr.insert(2, "haha")
arr.display()
arr.remove_by_index(3)
arr.remove_by_value("haha")
arr.display()
print(arr.search(5))
print(arr.search(2))
