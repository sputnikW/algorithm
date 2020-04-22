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
观察数学规律（或按照动态规划的思想去拆解子问题，会发现f(n) = f(n-1) + f(n-2)）发现是斐波那契数列，
普通递推求法是O(N)，用斐波那契数列公式可以到O(LogN)
空间复杂度上，可以用两个常量将空间保持在常数级

也可以用记忆化递归（标准的动态规划方式），也是O(N)的速度
"""