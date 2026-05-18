# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced = math.abs(height_left - height_right) <= 1
        # intutition --> calculate left and right height and then check, returning the height (1 + max(lefth, right)), boolean

        def dfs(root):
            # recursive implementation --> need to know the height and its balance
            if root is None:
                return (True, 0)
            
            balanced_l, height_l = dfs(root.left)
            balanced_r, height_r = dfs(root.right)

            balanced = (balanced_l and balanced_r) and abs(height_l - height_r) <= 1

            return (balanced, max(height_l, height_r) + 1)
        
        res = dfs(root)

        return res[0]