class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # can do two pointers or hash map / dictionary approach

        visited = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visited: # if the difference was already encountered, we've found a solution
                return [visited[diff], i]
            else: # add it to the dictionary, meaning it was'visited'
                visited[nums[i]] = i