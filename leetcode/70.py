class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n

        prev = 1
        curr = 2
        for i in range(3, n):
            temp = prev + curr
            prev = curr
            curr = temp
        
        return prev + curr

"""
O(N)
观察数学规律（或按照动态规划的思想去拆解子问题，会发现f(n) = f(n-1) + f(n-2)），发现是斐波那契数列，普通求法O(N)，用公式可以到O(LogN)
"""