import collections

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(dict)
        sortedQueue = collections.deque()
        for prerequisite in prerequisites:
            end, start = prerequisite
            graph[start][end] = None
        
        WHITE, BLACK, GARY = 0, 1, 2
        colors = [WHITE for i in range(numCourses)]

        def dfs(node): # return false if has circle
            colors[node] = GARY
            for end in graph[node]:
                if colors[end] == WHITE:
                    if not dfs(end):
                        return False
                elif colors[end] == GARY:
                    return False
            
            colors[node] = BLACK
            sortedQueue.appendleft(node)
            return True

        res = True
        for i in range(numCourses):
            if colors[i] == WHITE:
                if not dfs(i):
                    res = False
        return list(sortedQueue) if res else []


def main():
    so = Solution()
    so.canFinish(2, [[1, 0]])

if __name__ == "__main__":
    main()

"""
本质上是求一个有向图中，是否有环
方法是：
DFS遍历，如果在查看后驱节点时，发现了灰色节点，说明当前节点是从灰色来的，又能到灰色上去，则是一个环
"""