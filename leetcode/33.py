class Solution:
    def search(self, nums, target):
        # find the rotate pivot
        pivot = self.findPivot(nums)

        # binary search in logic position, only get value use true position
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            truePositionOfMid = self.getTruePosOfRotateArray(len(nums), pivot, mid)
            if target > nums[truePositionOfMid]:
                l = mid + 1
            elif target == nums[truePositionOfMid]:
                return truePositionOfMid
            else:
                r = mid - 1
        return -1

    # T = O(LogN)
    def findPivot(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # the pivot is at the right side
                l = mid + 1
            else:
                # the pivot is at the left of at mid

                # so first, check if the mid is the pivot
                if mid != 0 and nums[mid] < nums[mid - 1]:
                    return mid
                else:
                    # pivot still at th left
                    r = mid - 1
        # if can't find such pivot,means that the array is not rotate
        return 0

    def getTruePosOfRotateArray(self, numsLen, pivot, logicPos):
        if logicPos < numsLen - pivot:
            # means true position is at right of the pivot
            return logicPos + pivot
        else:
            # means true position is at left of the pivot
            return logicPos + pivot - numsLen

def main():
    testCases = [
        [4,5,6,7,0,1,2],
        [4,5,6,7,0,1,2, 3],
        [0,1,2, 3,4,5,6,7],
        [4,5,6,7,8,0,1,2,3]
    ];

    so = Solution()
    for case in testCases:
        print(so.search(case, 3))

if __name__ == "__main__":
    main();