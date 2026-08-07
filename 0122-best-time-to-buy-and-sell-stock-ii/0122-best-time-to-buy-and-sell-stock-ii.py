class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for i in range(1, len(prices)):
            daily_profit = prices[i] - prices[i - 1]
            if daily_profit > 0:
                total_profit += daily_profit

        return total_profit