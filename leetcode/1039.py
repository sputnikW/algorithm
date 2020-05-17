class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp = [
            [
                0 for j in range(len(A))
            ] for i in range(len(A)-1)
        ]

        for j in range(2, len(A)):
            for i in range(j-2, -1 ,-1):
                # k from i + 1 to j-1
                minRes = float('inf')
                for k in range(i+1, j):
                    minRes = min(A[i] * A[j] * A[k] + dp[i][k] + dp[k][j], minRes)
                dp[i][j] = minRes
        
        return dp[0][len(A)-1]
