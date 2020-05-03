class Solution:
    def canThreePartsEqualSum(self, A):
        tempSum = 0
        sums = []
        lenA = len(A)
        for i in range(lenA):
            tempSum += A[i]
            sums.append(tempSum)

        for i in range(1, lenA - 1):
            if sums[i] == (sums[lenA - 1] - sums[i]) * 2:
                for j in range(i):
                    if sums[j] == sums[i] - sums[j]:
                        return True

        return False

def main():
    testCases=[
        [3,3,6,5,-2,2,5,1,-9,4],
        [1,-1,1,-1]
    ]

    so = Solution()

    for case in testCases:
        print(so.canThreePartsEqualSum(case))

if __name__ == "__main__":
    main()

"""
T=O(N), S=O(N)
这里有两个比较关键的点： 
    - 每一个子数组的和都是: sum(A) / 3，这一点非常重要
    - 因为上面那一点有两个切分点，在找到一个切分点时，如果在这个切分点下找不到第二个切分点，就不可能再找到了

所以思路就变成了，从做往右，找sum/3 和 2 * sum/3 的两个位置

这题的关键在于：尽量少的做遍历数组中元素的操作，将暴力法中的遍历，想办法通过记录部分遍历得到的结果（在本题中，就是数组内所有元素的和）来避免掉
"""
