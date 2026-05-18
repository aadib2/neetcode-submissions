class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        f = 0
        b = len(heights) - 1

        while f < b:
            # calculate current area
            h = min(heights[f], heights[b])
            w = b - f
            curr_water = w * h

            # compare to max, update
            if curr_water > max_water:
                max_water = curr_water

            # if left height < right height, increment left pointer
            if heights[f] < heights[b]:
                f+=1
            else:
                # if right height <= left height, decrement right pointer
                b-=1
        return max_water

        