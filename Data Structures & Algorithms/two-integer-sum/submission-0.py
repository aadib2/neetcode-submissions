class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} # initialize dict
        
        # loop through array
        for i in range(len(nums)):
            diff = target - nums[i]
            # check if diff exists in dictionary as a key
            if (diff in dictionary):
                return [dictionary[diff], i] # if found return its index + our current index
            dictionary[nums[i]] = i
            