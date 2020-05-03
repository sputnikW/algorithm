class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right, mid = max(weights), sum(weights), 0
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if self.checkValidCapacity(D, mid, weights):
                right = mid - 1
                res = mid
            else:
                left = mid + 1

        return res
    

    def checkValidCapacity(self, days, capacity, weights):
        needDays = 1
        curDayCapacity = 0
        for weight in weights:
            if curDayCapacity + weight <= capacity:
                curDayCapacity += weight
            else:
                needDays += 1
                curDayCapacity = weight

        return needDays <= days;

"""
T=NLog(N)
题眼：
- 把问题转化为，做一个求最小值满足条件值的遍历，检查一个值的复杂度是O(N)
- 所有可选值是有序的且单调的（即x满足，所有大于x的也都满足），所以可以用二分查找减少遍历的次数
"""