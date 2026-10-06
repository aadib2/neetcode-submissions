class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hm: # its been seen before
                return [hm[diff], i]
            # else add it to hm
            hm[nums[i]] = i
        
        # guaranteed to have a solution so no need to return anything else
        