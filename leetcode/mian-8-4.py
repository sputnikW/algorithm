class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        prevSet = [[nums[0]]]
        for i in range(1, len(nums)):
            newSet = [ [nums[i]] ]
            for set in prevSet:
                newSet.append(set + [nums[i]])
            prevSet += newSet
        
        return [[]] + prevSet

