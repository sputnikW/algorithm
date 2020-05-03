class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenNums = len(nums)
        if lenNums == 1:
            return

        maxFromTail = -1

        for i in range(lenNums - 2, -1, -1):
            maxFromTail = max(nums[i + 1], maxFromTail)
            if nums[i] < maxFromTail:
                # find the closest number in the end of array form right to left
                indexOfminDelta = -1
                for j in range(lenNums - 1, i, -1):
                    if nums[j] - nums[i] > 0:
                        indexOfminDelta = j
                        break
                # swap curr number with the closest number
                temp = nums[indexOfminDelta]
                nums[indexOfminDelta] = nums[i]
                nums[i] = temp

                # reverse the right part asc in-place
                k, l = i + 1, lenNums - 1
                while k < l:
                    temp = nums[k]
                    nums[k] = nums[l]
                    nums[l] = temp
                    k += 1
                    l -= 1
                return

        nums.reverse()
        return

"""
T=O(N)
"""