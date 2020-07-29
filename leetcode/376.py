UP, DOWN, FLAT = 0, 1, 2

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        
        direct = self.getDirect(nums[0], nums[1])
        maxLen = 1 if direct == FLAT else 2

        if len(nums) == 2:
            return maxLen

        for i in range(2, len(nums)):
            newDirect = self.getDirect(nums[i-1], nums[i])
            if newDirect == FLAT:
                continue
            if newDirect != direct:
                direct = newDirect
                maxLen += 1

        return maxLen


    def getDirect(self, front, before):
        diff = before - front
        if diff < 0:
            return DOWN
        elif diff == 0:
            return FLAT
        else:
            return UP
