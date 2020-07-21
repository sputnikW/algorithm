# import collections
import queue

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 用邻接hash表来存储图
        graph = {}
        for time in times:
            start, end, cost = time
            if start not in graph:
                graph[start] = {}
            graph[start][end] = cost


        # Dijkstra
        q = queue.PriorityQueue() # (cost, vertex)
        for i in range(1, N+1):
            if i == K:
                q.put((0, i))
            else:
                q.put((float('inf'), i))

        maxCost = 0

        while not q.empty():
            cost, start = q.get()
            maxCost = max(cost, maxCost)
            
            if start not in graph:
                continue
            for end in graph[start]:
                # relax
                



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