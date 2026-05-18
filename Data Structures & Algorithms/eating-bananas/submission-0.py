class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # possible approach
        # piles[i] / k = h
        # increment until get to an eating rate whose total_hours <= h

        # brute force
        # check every value of k until get to m
        # upper bound would be max pile 

        # better way is to split the max in half and if total_hours > h (increase k) or if total_hours < h (decrease k)
        high_k = max(piles) # upper bound
        low_k = 1
        res  = high_k # init to the worst case

        # find the middle
        # total number of hours (go through the list completely) and for each get ceiling(piles[i]  / k)
        # add to total
        while low_k <= high_k:
            curr_k = (low_k + high_k) // 2

            curr_hours = 0
            for pile in piles:
                curr_hours += math.ceil(pile / curr_k)
            
            if curr_hours > h:
                # need to increase k, so look at right side of values
                low_k = curr_k + 1
            else: #if it is smaller than the time or equal to, look for a smaller k
                high_k = curr_k - 1
                res = curr_k
        
        return res




