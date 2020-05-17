class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        elif len(grid[0]) == 0:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                totalCost = grid[i][j]
                minPrevCost = 0 if i==0 and j ==0 else float('inf')
                if i > 0:
                    minPrevCost = min(minPrevCost, grid[i-1][j])
                if j > 0:
                    minPrevCost = min(minPrevCost, grid[i][j-1])
                grid[i][j] = totalCost + minPrevCost

        return grid[-1][-1]