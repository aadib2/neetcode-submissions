from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        result = [] # result list

        # add root to queue
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []

            for i in range(level_size):
                top = queue.popleft()
                current_level.append(top.val)

                # add children nodes
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            
            result.append(current_level)
        return result

        

        