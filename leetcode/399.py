class Solution:
    def calcEquation(self, equations, values, queries):
        WHITE, GARY, BLACK = (0, 1, 2)

        # 因为不确定有多少节点，所以只能用邻接表来存储图
        graph = {}
        colors = {}
        for i in range(len(equations)):
            equation = equations[i]
            start, end = equation

            # 因为从start到end和从end到start的权重是不一样的，所以应该是有向边；且query的也有可能是两个方向，所以两个方向的边都要记录
            if start not in graph:
                graph[start] = {}
            if end not in graph:
                graph[end] = {}
            # 因为要存储边的权重，所以没用数组，用了哈希表
            graph[start][end] = values[i]
            graph[end][start] = 1 / values[i] # 反向的话就是倒数

            # 染色，准备dfs
            colors[start] = WHITE
            colors[end] = WHITE

        # dfs，返回路径的权重之和, 未找到则return 0
        def dfs(vertex, target, currColors):
            nonlocal colors
            nonlocal graph

            # 点不在图里 or 点没有和其他点相连
            if vertex not in colors or target not in colors or vertex not in graph or target not in graph:
                return 0

            if vertex == target:
                return 1
            currColors[vertex] = GARY
            for end in graph[vertex].keys():
                edgeVal = graph[vertex][end]
                if currColors[end] == WHITE:
                    subVal = dfs(end, target, currColors)
                    if subVal: # 如果内层找到了
                        return subVal * edgeVal

            currColors[vertex] = BLACK
            return 0

        res = []
        for query in queries:
            start, target = query
            currColors = colors.copy()
            val = dfs(start, target, currColors)
            if val:
                res.append(val)
            else:
                res.append(-1.0)
        
        return res


def main():
    so = Solution()
    so.calcEquation(
        [["a","b"],["b","c"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    )

if __name__ == "__main__":
    main()


"""
TODO: 看一下huahua并查集的解法
思路：
题目可抽象为：求一个图中，从一点到另一点的路径的权重之积，如果无法到达另外一个点，则返回一个特殊值
题目有一个前提条件：no contradiction，说明一个点到另一个点的路径之积一定是相同的（如果有多条路径的话）

首先肯定要:
- 构造一个图
- 然后从query的起点开始，搜索终点
    - 记录路径的权重之积
    - 如果搜索不到，则返回特殊值
估一下时间复杂度：找路径一次是V+E，如果query多了，在遍历的过程中可以做记忆化（起点到每一个点的路径权重之积），但空间占用量是V^2,点多了可能有点吃不消
"""