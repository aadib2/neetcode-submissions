class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first need to find the 'target' row between 0 and m-1
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bot = m - 1

        mid_i = top # by default it is equal to the first one (takes care of base case if equal)

        while top <= bot:
            mid_i = (top + bot) // 2
            
            if target < matrix[mid_i][0]:
                bot = mid_i - 1
            elif target > matrix[mid_i][n-1]:
                top = mid_i + 1
            else:
                break # we are in the target row
        
        # perform binary search on target row
        left = 0
        right = n-1

        row = (top + bot) // 2

        while left <= right:
            mid_j = (left + right) // 2

            if target == matrix[row][mid_j]:
                return True
            elif target < matrix[row][mid_j]:
                right = mid_j - 1
            else:
                left = mid_j + 1
        
        return False


            