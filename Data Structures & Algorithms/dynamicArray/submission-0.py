class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # total space available
        self.size = 0 # number of elements used 
        self.arr = [None] * capacity 

    def get(self, i: int) -> int:
        if i >= 0 and i < self.size: # get element if i is within usable range
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i >= 0 and i < self.size: # set i if in usable range (elements are continguous)
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity: # resize if full 
            self.resize()

        self.arr[self.size] = n # insert at end 
        self.size += 1

    def popback(self) -> int:
        if self.size > 0: 
            val = self.arr[self.size - 1]
            self.size -= 1
            return val

    def resize(self) -> None:
        self.capacity *= 2 
        new_arr = [None] * self.capacity # resize new array

        for i in range(self.size): # copy elements 
            new_arr[i] = self.arr[i]

        self.arr = new_arr 

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity