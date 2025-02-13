class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        res = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                res = max(res, profit)
            else: # prices are equal or buying > sell = negative profit
                left = right
            right += 1
        
        return res

# Time = O(n), Space = O(1)