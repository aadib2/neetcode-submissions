class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None: # base case: empty list
            return -1
        
        curr = self.head # starting node
        for i in range(index): # when the loop stops, curr = Node at index i
            if curr.next is None:
                return -1
            curr = curr.next

        return curr.data # important: return the value not the node itself

    def insertHead(self, val: int) -> None:
        new = Node(data=val) # create new node based on val

        # if head exists or doesn't it still works
        new.next = self.head
        self.head = new

    
    def insertTail(self, val: int) -> None:
        # create new node based on val
        new = Node(data=val)

        if self.head is None:
            self.head = new
            return
        
        # otherwise, traverse till we get to the end
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        
        # now at last element, so insert "new" at tail
        curr.next = new
        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        
        # handle index 0
        if index == 0:
            self.head = self.head.next
            return True
        
        prev = None
        curr = self.head

        for i in range(index): # loop will iterate index+1 times
            if curr.next is None: # the index must be out of bounds
                return False
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        del curr

        return True
        

    def getValues(self) -> List[int]:
        output = []

        if self.head is None:
            return output

        curr = self.head
        while curr is not None:
            output.append(curr.data)
            curr = curr.next
        return output
        
