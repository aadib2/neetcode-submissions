class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {']': '[', ')': '(', '}': '{'}

        stack = []
        for c in s:
            if c in mapping: # if it is a closing bracket
                if len(stack) == 0 or stack[-1] != mapping[c]: # if there are too many closing or wrong ordering
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        return False

        