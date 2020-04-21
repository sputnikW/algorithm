class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: # 0, 1
            return x

        left = 2
        right = x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < x:
                left = mid + 1
            elif square > x:
                right = mid - 1
            else:
                return mid

        return right

"""
O(LogN)
这里肯定不能直接用sqrt函数
这是一个比较简单的思路，从0，一直找到平方接近x的整数，但是对于比较大的数，可能要进行几百万几千万次计算才能找到
而由于整数是天然有序的，可以用二分查找算法，将复杂度压缩到LogN
"""
