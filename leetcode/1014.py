class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxInPrev = 0
        res = 0

        for j in range(1, len(A)):
            prevIndex = j - 1
            maxInPrev = max(A[prevIndex] + prevIndex, maxInPrev)
            res = max(res, maxInPrev + A[j] - j)

        return res

"""
T=O(N)
题眼：
- 求数组中任意两个组合的最大值
- 相比与暴力两重循环的方法，然而有一层循环的最优解可以直接取到，所以这重循环可以不用遍历
"""