class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) < 3:
            return max(nums)

        theDayBeforeYesterday, yesterday = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # 根据前面两个最优解，计算当前的最优解
            curr = max(theDayBeforeYesterday + nums[i], yesterday)
            theDayBeforeYesterday = yesterday
            yesterday = curr

        return curr
