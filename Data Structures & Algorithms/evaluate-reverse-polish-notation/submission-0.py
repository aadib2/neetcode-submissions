class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # can implement as list
        res = 0

        for c in tokens:
            if not self.is_integer(c):
                # pop top two elements from stack
                op2 = stack.pop()
                op1 = stack.pop()

                if c == '+':
                    res = op1 + op2
                elif c == '-':
                    res = op1 - op2
                elif c == '*':
                    res = op1 * op2
                else:
                    # must be division
                    res = int(op1 / op2) # since both are integers we need to ensure output is also int
                
                stack.append(res)
            else:
                stack.append(int(c))
        
        return stack.pop() # return the top element
                


    def is_integer(self, s) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False