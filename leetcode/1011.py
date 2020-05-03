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