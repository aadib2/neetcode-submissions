# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base cases
        if not head or head.next == None: # either empty or only one node
            return head

        curr = head
        prev = None

        while (curr != None):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        head = prev

        return head
        

        