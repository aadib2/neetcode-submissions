# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # case for empty
        if head == None:    
            return False

        # case for 1 node that doesn't point to anything
        if head.next == None:
            return False

        # case if head points to itself
        if head.next == head:
            return True

        
        fast = head
        slow = head

        while fast and fast.next != None: # need to check if both exist
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        
        return False
