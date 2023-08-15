class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit