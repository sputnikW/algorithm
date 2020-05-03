class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lenNums = len(nums)
        if lenNums < 4:
            return []

        res = []
        nums.sort()

        prevK, prevL, prevI, prevJ = None, None, None, None

        for k in range(lenNums - 3):
            # 跳过相同的值
            if prevK != None and prevK == nums[k]:
                continue
            prevK = nums[k]
            prevL = None # 当第二层遍历完一遍后，再执行到这，k肯定变了，所以应该重置L的上一个值

            for l in range(k+1, lenNums - 2):
                # 跳过相同的值
                if prevL != None and prevL == nums[l]:
                    continue
                prevL = nums[l]

                sumKL = nums[k] + nums[l]
                i = l + 1
                j = lenNums - 1
                prevI = None # 新的一轮遍历重置上一个的值
                prevJ = None # 同上
                while i < j:
                    # 跳过相同的值
                    if prevI != None and prevI == nums[i]:
                        i += 1
                        continue
                    if prevJ != None and prevJ == nums[j]:
                        j -= 1
                        continue

                    prevI = nums[i]
                    prevJ = nums[j]

                    sum = sumKL + nums[i] + nums[j]
                    if sum > target:
                        j -= 1
                        prevI = None # 因为只移动了j，所以i的值肯定没变，为了跳过下一轮对i的检查，将prevI设置为None，下同
                    elif sum == target:
                        res.append([nums[k], nums[l], nums[i], nums[j]])
                        i += 1
                        prevJ = None
                    else:
                        i += 1
                        prevJ = None

        return res

"""
T=O(N^3)

算法比较暴力了
- 总共4层遍历，最里面两层是一个求数组两元素之和满足固定条件的所有可能组合，用双指针法把算法复杂度减到O(N)
- 比较关键的在于如何去除重复的解，在任何一层的一次遍历内，如果出现了相同的值，应该直接跳过，避免该层取了重复的值
"""