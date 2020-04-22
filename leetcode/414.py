class Solution:
    def thirdMax(self, nums) -> int:
        numsLen = len(nums)

        if numsLen == 1:
            return nums[0]
        elif numsLen == 2:
            return max(nums[0], nums[1])
        else:
            first, second, third = None, None, None
            for i in range(numsLen):
                num = nums[i]
                if first == None or num > first:
                    third = second
                    second = first
                    first = num
                elif second == None or num > second:
                    if num != first:
                        third = second
                        second = num
                elif third == None or num > third:
                    if num != second:
                        third = num
            return third if third != None else first

def main():
    testCases = [
        [1],
        [-1, -10],
        [-10,-22,1,3,2,69,34],
        [2,2,3,1],
        [1,1,2]
    ]

    so = Solution()

    for case in testCases:
        print(so.thirdMax(case));

if __name__ == "__main__":
    main()

"""
T: O(N)
S: O(1)
这题有个陷阱，1、2、3大的数不能重复，且有可能虽然数组数量大于3，但实际只有两个数值，也是没有第3大的数
"""