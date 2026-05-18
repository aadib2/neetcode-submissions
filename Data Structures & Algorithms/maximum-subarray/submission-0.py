class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # follow a "sliding window" logic with two pointers
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                # reset it
                currSum = 0
            currSum += num
            if currSum > maxSum:
                maxSum = currSum
        
        return maxSum
        
        