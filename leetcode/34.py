class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        #first, find the most left target
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                start = mid
                break
            else:
                right = mid - 1
        if start == -1:
            # can't find start, return
            return [-1, -1]

        # find the end of target
        left, right = start, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target and (mid == len(nums) - 1 or nums[mid+1] != target):
                end = mid
                break
            else:
                left = mid + 1

        return [start, end]

"""
T=O(logN)
因为有时间复杂度要求，所以想到binary search，比较特殊的是，判断是否找到的条件有一点点特殊
"""
