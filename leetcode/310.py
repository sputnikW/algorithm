import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        heightOfRoot = [-1 for i in range(n)]

        graph = collections.defaultdict(dict)
        graph[0] = {} # 处理一个edge case：只有一个点，没有边，其他情况下应该所有点都在某条边上
        for edge in edges:
            left, right = edge
            graph[left][right] = None
            graph[right][left] = None

        while len(graph.keys()) > 2: # 持续这个操作，直到还剩下小于两个节点
            waitingForDel = []
            for node in graph:
                if len(graph[node]) == 1: # 如果有节点只和一条边相连，则删除这个节点
                    waitingForDel.append(node) # 先记下来，统一删除
            
            for node in waitingForDel:
                # 删除点和与该点相接的边
                for end in graph[node]: # 聚合分析，O（E）
                    del graph[end][node]
                del graph[node] # 这里能保证被删除的node一定不会与其他待删除的node相连

        return [node for node in graph]

"""
S = O(N^2 + E)

参考leetcode更佳的写法：
- 用一个set保存和该节点相邻的点，插入和删除都是O-1
- 每轮循环，不去检查所有的节点，而是检查与1度节点相邻的节点。——通过聚合分析，发现复杂度降到了O（N）
"""


        # def bfs(root): # 返回在root确定的前提下，最长的最短路径
        #     visited = {}
        #     queue = collections.deque() # (vertex, distance)

        #     queue.append((root, 0))
        #     maxDist = 0
        #     visited[root] = None
        #     while len(queue):
        #         start, dist = queue.popleft()
        #         for end in graph[start]:
        #             if end not in visited:
        #                 queue.append((end, dist+1))
        #                 maxDist = max(maxDist, dist+1)
        #                 visited[end] = None
        #     return maxDist
        
        # minHeights = [bfs(vertex) for vertex in range(n)]

        # minHeight = float('inf')
        # minHeightVertex = []
        # for i in range(len(minHeights)):
        #     height = minHeights[i]
        #     if height < minHeight:
        #         minHeight = height
        #         minHeightVertex = [i]
        #     elif height == minHeight:
        #         minHeightVertex.append(i)

        # return minHeightVertex
                    


        

"""
本质上，是一个求所有节点之间的最短路径的问题
因为是无权重的图，一次单源最短路径计算只需要V+E的时间，所以可以通过多次单源最短路径计算来实现，时间复杂度是V(V+E)
"""