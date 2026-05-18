class DynamicArray:
    
    def __init__(self, capacity: int):
        # can use python list
        self.arr = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == len(self.arr):
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        temp = self.arr[self.size-1]
        self.arr[self.size-1] = None # set the last value to None (still keeps same capacity)
        self.size -= 1
        return temp

    def resize(self) -> None:
        # add twice the number of values
        self.arr = self.arr + ([None] * len(self.arr))

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return len(self.arr)
