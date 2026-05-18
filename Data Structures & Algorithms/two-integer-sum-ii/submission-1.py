class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # can use two pointers technique where front = 0 and back = len - 1
        # check each pair and control pointers

        f = 0
        b = len(numbers) - 1

        while f < b:
            sum = numbers[f] + numbers[b]
            if sum > target:
                b-=1
            elif sum < target:
                f+=1
            else: # target was found
                return [f+1, b+1]
        
        # if there isn't a solution
        return []

        # binary search
