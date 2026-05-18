class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # implement divide and conquer method that went over in class
        max_profit = 0

        # brute force
        # for i in range(0, len(prices) - 1):
        #     for j in range(i+1, len(prices)):
        #         curr_profit = prices[j] - prices[i]

        #         if curr_profit > max_profit:
        #             max_profit = curr_profit
        
        # return max_profit

        # two pointers
        left = 0
        right = 1
        n = len(prices)
        max_profit = 0

        while right < n:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right # move left pointer over (sort of a sliding window)
            right+=1

        return max_profit
