class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0

        minBuyPrice = prices[0]
        maxProfitPrice = 0
        for i in range(1, len(prices)):
            maxProfitPrice = max(prices[i] - minBuyPrice, maxProfitPrice)
            minBuyPrice = min(minBuyPrice, prices[i])

        return maxProfitPrice

def main():
    tCs = [
        [1,2]
    ]

    so = Solution()
    for case in tCs:
        print(so.maxProfit(case))

if __name__ == "__main__":
    main()

"""
注意BugFree，在题目没特别说明边界情况的前提下，所有可能的输入都要考虑
"""