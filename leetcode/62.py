class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [
            [
                1 for i in range(m)
            ] for j in range(n)
        ]

        for i in range(1, n):
            for j in range(m):
                curPathCount = map[i-1][j]
                if j > 0:
                    curPathCount += map[i][j-1]
                map[i][j] = curPathCount
        
        return map[n-1][m-1]
