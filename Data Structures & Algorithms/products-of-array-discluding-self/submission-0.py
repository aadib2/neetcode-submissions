class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        
        # prefix = [1] # first will always be 1
        # suffix = [1] # first will also always be 1

        # # prefix loop
        # for i in range(1, len(nums)):
        #     prefix.append(nums[i-1] * prefix[i-1])
        
        # # suffix loop (reverse order)
        # for i in range(len(nums) - 2, -1):
        #     suffix.insert(0, nums[i+1] * suffix)
            
        
        # return res

        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res

        