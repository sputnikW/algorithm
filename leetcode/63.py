class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0:
            return 0
        elif len(obstacleGrid[0]) == 0:
            return 0
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    totalPaths = 1 if i==0 and j==0 else 0
                    if i > 0:
                        totalPaths += obstacleGrid[i-1][j]
                    if j > 0:
                        totalPaths += obstacleGrid[i][j-1]
                    obstacleGrid[i][j] = totalPaths
        
        return obstacleGrid[-1][-1]

def main():
    testCase = [[0,0,0],[0,1,0],[0,0,0]]

    so = Solution()
    print(so.uniquePathsWithObstacles(testCase))

if __name__ == "__main__":
    main()