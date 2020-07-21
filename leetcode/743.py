import collections
import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        # 用邻接hash表来存储图
        graph = collections.defaultdict(dict)
        for time in times:
            start, end, cost = time
            if start not in graph:
                graph[start] = {}
            graph[start][end] = cost

        # Dijkstra
        heap = [] # (cost, vertex)
        maxCost = 0
        costs = {}
        heapq.heappush(heap, (0, K))

        while heap:
            cost, start = heapq.heappop(heap)
            
            if start in costs: # 如果当前点已经有了确定的最短路径，则直接放弃（某种意义上的松弛）
                continue

            maxCost = max(cost, maxCost)
            costs[start] = cost

            # 根据已有确定解的节点求其他解

            for end in graph[start]: # 所有当前确定的最短路径的点的后置节点
                # relax
                if end in costs: # 如果后置节点已经有了最短路径值，则不再处理
                    continue
                # 否则则将可能是更小路径值的塞进去（松弛，只不过把可能的值都放到了堆里，由于堆的性质，能保证一个节点总是先访问最小的值，其他值会被放弃）
                heapq.heappush(heap, (cost + graph[start][end]))

        return maxCost if len(cost) == N else -1

        # BFS
        # WHITE, BLACK, GARY = 0, 1, 2
        # colors = [WHITE for i in range(N+1)]

        # maxCost = 0
        # queue = collections.deque()
        # # init
        # queue.append((K, 0)) # (node, cost)
        # colors[K] = GARY
        # dirtyNodeCount = 1
        # while len(queue):
        #     start, cost = queue.popleft()
        #     if start not in graph: # has no edge
        #         continue
        #     for end in graph[start]:
        #         if colors[end] == WHITE:
        #             newCost = cost + graph[start][end]
        #             maxCost = max(newCost, maxCost)
        #             queue.append((end, newCost))
        #             colors[end] = GARY
        #             dirtyNodeCount += 1

        # return maxCost if dirtyNodeCount == N else -1

"""
没啥好说的，带权的单源最短路径问题
"""