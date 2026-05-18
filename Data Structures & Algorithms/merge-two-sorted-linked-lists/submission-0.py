# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # treat it like merge sort
        dummy = ListNode() # starting with dummy node
        tail = dummy
    

        while list1 and list2:
            if list1.val <= list2.val:
                # append curr1 to merged
                tail.next = list1
                list1 = list1.next
            else:
                # append curr2 to merged
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # copy remaining nodes in list1 if needed
        if list1:
            tail.next = list1
        
        # copy remaining nodes in list2 if needed
        if list2:
            tail.next= list2

        return dummy.next
        