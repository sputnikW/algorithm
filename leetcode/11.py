class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0

        while i < j:
            res = max(
                min(height[i], height[j]) * (j - i),
                res
            )
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res



"""
关键：
- 暴力法是求数组中的两个数所有可能的组合
- 然而有一种方法，可以用常数级的复杂度，排除掉某一个数与其他数所有不是最优解的组合（通过某种逻辑）
- 只对剩下所有可能是最优解的组合进行计算（这种遍历通过双指针的方式）

总结：通过逻辑，排除所有不可能是最优解的情况，从而减少不必要的遍历（通过其他比较奇特的遍历方式）

关键词：两个元素的可能组合，双指针
"""