class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        lenNums = len(nums)

        nums.sort()
        prevTarget = None
        for k in range(lenNums):
            target = nums[k]

            if prevTarget != None and target == prevTarget:
                continue

            prevTarget = target

            if target > 0:
                break

            i = k + 1
            j = lenNums - 1

            prevNumI, prevNumJ = None, None

            while i < j:
                if prevNumI != None and nums[i] == prevNumI:
                    # 说明这一步会得到和上一步一样的结果，那直接跳过
                    i += 1
                    continue
                elif prevNumJ != None and nums[j] == prevNumJ:
                    # 说明这一步会得到和上一步一样的结果，那直接跳过
                    j -= 1
                    continue

                currSum = nums[i] + nums[j]
                prevNumI = nums[i]
                prevNumJ = nums[j]
                if currSum < -target:
                    # 说明i太小了，i应该往后靠
                    i += 1
                    prevNumJ = None
                elif currSum == -target:
                    #说明刚好
                    res.append([target, nums[i], nums[j]])
                    i += 1
                    prevNumJ = None
                else:
                    #说明j太大了
                    j -= 1
                    prevNumI = None

        return res

"""
T=O(N^2)，Fxxx,原来还有复杂度是N^2就能过的解法
关键：
- 原来是个N^3的算法，3层遍历，想办法减少某层遍历的复杂度
- 有两层遍历解决的抽象问题是：求数组中两个元素的组合，满足某个条件
    - 这个问题有个特征，元素的顺序并不重要
    - 需要找出所有可能的组合
    - 可以在排序后，通过逻辑过滤掉某些完全不可能的组合来遍历（通过双指针的方式）

总结：
- 双指针 -> 最优解、所有解
"""