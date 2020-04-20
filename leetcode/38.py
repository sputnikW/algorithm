class Solution:
    def getNext(self, numStr: str) -> str:
        lenOfNumStr = len(numStr)

        res = ''
        point = 0
        curCount = 0

        while point < lenOfNumStr:
            isLast = point == lenOfNumStr - 1

            curDigit = numStr[point]
            nextDigit = numStr[point + 1] if not isLast else None

            curCount += 1

            if isLast:
                res += str(curCount) + curDigit
            else:
                if curDigit != nextDigit:
                    res += str(curCount) + curDigit
                    curCount = 0

            point += 1
        return res


    def countAndSay(self, n: int) -> str:
        res = '1'

        for i in range(n - 1):
            res = self.getNext(res)

        return res;

def main():
    so = Solution()

    for i in range(30):
        print(so.countAndSay(i + 1))

if __name__ == "__main__":
    main()

# O(N * M) M为求的是序列中的第几位