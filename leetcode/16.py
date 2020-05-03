class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        lenNums = len(nums)

        closestDelta = float('inf')
        sumForclosest = 0

        for k in range(len(nums)):
            i = k + 1
            j = lenNums - 1

            while i < j:
                sum = nums[i] + nums[j] + nums[k]
                delta = target - sum
                if abs(delta) < closestDelta:
                    closestDelta = abs(delta)
                    sumForclosest = sum

                if delta == 0:
                    return sum
                elif delta > 0:
                    i += 1
                else:
                    j -= 1

        return sumForclosest

"""
T=O(N^2)
关键：
- 顺序不重要 -> 是不是要排序?
- 求数组两个元素的组合的最优解-> 双指针
"""