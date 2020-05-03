class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        squareAmountIfCurrAsRightBottom = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
                        res += squareAmountIfCurrAsRightBottom
                        matrix[i][j] = squareAmountIfCurrAsRightBottom

        return res

"""
T=O(M * N)

关键：
- 很容易可以发现，更大的问题的解可以得出更小的问题的解->能不能通过较小问题的解得到更大问题的解（难点）
- DP，去找状态转移公式，找到后就可以解了

关键词：计数，大问题感觉似乎能覆盖一些小问题的解，DP
"""