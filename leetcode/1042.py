class Solution:
    def gardenNoAdj(self, N, paths):
        res = [
            [1,2,3,4] for i in range(N)
        ]

        pathMap = {}
        for i in range(N):
            pathMap[i+1] = []

        for path in paths:
            pathMap[path[0]].append(path[1])
            pathMap[path[1]].append(path[0])

        for i in range(1, N + 1):
            res[i-1] = res[i-1][0]
            for connectV in pathMap[i]:
                if connectV > i and res[i-1] in res[connectV-1]:
                    res[connectV-1].remove(res[i-1])
        
        return res

def main():
    so = Solution()
    so.gardenNoAdj(5,[[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]])

if __name__ == "__main__":
    main()