class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        startOfZero = -1
        for i in range(len(nums)):
            num = nums[i]

            if num == 0 and startOfZero == -1:
                startOfZero = i
            elif num != 0 and startOfZero > -1:
                nums[startOfZero] = num
                nums[i] = 0
                startOfZero += 1

"""
T：O(N)
S：O(1)
"""