class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True

        for i in range(len(nums)):
            nums[i] = i + nums[i]
        current = 0 # the most far distance of current is nums[current]
        while current < len(nums)-1 and current != nums[current]:
            # until to the end or dead
            maxDist = -1
            maxDistIndex = -1
            for i in range(current+1, min(nums[current]+1, len(nums))):
                if nums[i] > maxDist:
                    maxDist = nums[i]
                    maxDistIndex = i
            current = maxDistIndex
        
        return True if current == len(nums)-1 else False