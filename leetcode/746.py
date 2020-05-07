class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0 # dp(0)
        curr = 0 # dp(1)
        for i in range(2, len(cost) + 1):
            temp = min(prev + cost[i-2], curr + cost[i-1])
            prev = curr
            curr = temp

        return curr

"""
T=O（N）
递推的dp，思路很简单，看dp（N）有几种可能，取所有可能的最优解，即得到了状态转移方程
另外一个比较关键的是，这里的N是len（从0开始），需要明确题目的意思，所以dp（0）的cost数组其实是一个空数组，dp（1）意味着仅有一级台阶，到达一级台阶的顶点（第二级）
"""
