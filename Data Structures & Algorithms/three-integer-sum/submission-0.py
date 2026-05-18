class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers
        # should be O(n^2)
        # try brute force -> would be O(n^3)

        

        #   method for two sum if sorted used two pointers (might be the method here) 
        # but with two for loops

        # potentially sort the array -> then solve through pointers approach

        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l +=1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
            
        return result



        

