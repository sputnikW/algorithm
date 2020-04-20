class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        import sys
        nums.append(sys.maxsize)

        for i in range(len(nums) - 1):
            num = nums[i]
            nextBiggerNum = nums[i + 1]

            if target == num:
                return i
            elif num < target < nextBiggerNum:
                return i + 1
            elif target < num:
                return 0

# O(N)