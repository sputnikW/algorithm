class Solution:
    def plusOne(self, digits):
        # here we will not make this function as pure function for simple
        biggerThanTenAfterPlus = False

        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            biggerThanTenAfterPlus = digit == 9
            if biggerThanTenAfterPlus:
                digits[i] = 0
            else:
                digits[i] = digit + 1
                biggerThanTenAfterPlus = False
                break

        if biggerThanTenAfterPlus:
            digits.insert(0, 1)

        return digits

def main():
    testCases = [
        [1,2,3],
        [1,9,9,9],
        [1,2,4,9],
        [0],
        [99],
        [4],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

    so = Solution()
    for case in testCases:
        res = so.plusOne(case)
        print(''.join(str(num) for num in res))


if __name__ == "__main__":
    main()

"""
O(N)
如果需要在数组的开头增加一个数字，insert这个操作是O(N)的，
这里需要注意一个测试case，即数字位数非常大，可能不能被正常地转成int类型，所以不能先转成数字再计算
"""