class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val) # add to end of list, which is 'top' of stack

        # when pushing compare to minimum
        if len(self.minStack) == 0 or val < self.minStack[-1]:
            self.minStack.append(val)
        else: # else just push the current min
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # return min(self.stack) # will run in O(n) time but need O(1)
        return self.minStack[-1]
        
