class Solution:
    # traverse in map, and set all empty cell to the sum of it's top,left,right,bottom, return the sum of the sub sum
    def setInsideMapAndGetCount(self, prevMap, x_start, x_end, y_start, y_end, m, n):
        initMap = [
            [
                0 for j in range(n)
            ] for i in range(m)
        ]
        totalSum = 0
        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                if prevMap[y][x] == 0:
                    if y > y_start:
                        initMap[y][x] += prevMap[y-1][x]
                    if y < y_end:
                        initMap[y][x] += prevMap[y+1][x]
                    if x > x_start:
                        initMap[y][x] += prevMap[y][x-1]
                    if x < x_end:
                        initMap[y][x] += prevMap[y][x+1]
                    totalSum += initMap[y][x]
        return (totalSum, initMap)

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if N == 0:
            return 0

        leftEdgeOfX, rightEdgeOfX = 0, n - 1
        topEdgeOfY,  bottomEdgeOfY = 0, m - 1

        prevInsideCounts = 1
        allOutCounts = 0

        curMap = None
        prevMap = [
            [
                0 for j in range(n)
            ] for i in range(m)
        ]
        prevMap[i][j] = 1

        for step in range(1, N+1):
            curInsideCounts, curMap = self.setInsideMapAndGetCount(
                prevMap,
                max(leftEdgeOfX, j-step),
                min(rightEdgeOfX, j+step),
                max(topEdgeOfY, i-step),
                min(bottomEdgeOfY, i+step),
                m,
                n
            )
            allOutCounts += prevInsideCounts * 4 - curInsideCounts
            allOutCounts = allOutCounts % (pow(10, 9) + 7)
            prevMap = curMap
            prevInsideCounts = curInsideCounts
        
        return allOutCounts