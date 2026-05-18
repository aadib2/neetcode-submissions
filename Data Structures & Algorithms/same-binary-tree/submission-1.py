from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive solution

        # base cases
        # if p is None and q is None:
        #     return True
        # if p is None or q is None:
        #     return False

        # if p.val != q.val:
        #     return False
        # else: # if they are equal
        #     # check their left and right children
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # alternate way is using a queue (BFS logic)
        # use two queues?

        dq = deque([(p, q)])

        while dq:
            n1, n2 = dq.popleft()

            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False

            dq.append((n1.left, n2.left))
            dq.append((n1.right, n2.right))

        return True

                

