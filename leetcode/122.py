class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        sum = 0
        for i in range(1, len(prices)):
            profitToday = prices[i] - prices[i-1]
            if profitToday > 0:
                sum += profitToday
        
        return sum
