class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        rows = len(obstacleGrid)
        if not rows:
            return []
        cols = len(obstacleGrid[0])
        if not cols:
            return []
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] == 1:
                        return []
                    else:
                        obstacleGrid[i][j] = [[i,j]]
                        continue
                
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = []
                elif i-1 >= 0 and len(obstacleGrid[i-1][j]) > 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + [[i, j]]
                elif j-1 >= 0 and len(obstacleGrid[i][j-1]) > 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + [[i, j]]
                else:
                    obstacleGrid[i][j] = []

        return obstacleGrid[rows-1][cols-1]
                