class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA = len(a)
        lenB = len(b)
        res = ''

        # unshift 0 for the short str, make two str is same long
        prefixZero = ''.join(
            '0' for _ in range(abs(lenA - lenB))
        )
        if lenA > lenB:
            b = prefixZero + b
        else:
            a = prefixZero + a

        overflowBit = 0

        for i in range(max(lenA, lenB) - 1, -1, -1):
            bitOfA = a[i]
            bitOfB = b[i]
            sum = int(bitOfA) + int(bitOfB) + overflowBit
            if sum == 3:
                res = '1' + res
                overflowBit = 1
            elif sum == 2:
                res = '0' + res
                overflowBit = 1
            else:
                res = str(sum) + res
                overflowBit = 0

        if overflowBit == 1:
            res = '1' + res

        return res

def main():
    testCase = [
        ['1', '1'],
        ['1', '0'],
        ['100000000000', '1'],
        ['111111', '1'],
        ['100', '10000000'],
        ['1111', '1111']
    ]

    so = Solution()
    for case in testCase:
        print(so.addBinary(case[0], case[1]))

if __name__ == "__main__":
    main()

"""
O(N)
需要注意测试case写全，同位相加再加上进位后之和可能是3，这种情况需要注意
此算法主要是为了便于理解，实际上完全不需要补0耗费多余的空间
并且当较短的数累加完之后，如果不需要进位可以直接拼接甚于字符串返回，以此加快部分case的速度

有两个写法上可以优化的点：
- n个0组成的字符串可以直接 0 * n
- for循环里的if判断那里，可以不写的这么暴力（针对每个case），而是用sum%2求当前位，sum // 2求进位
"""