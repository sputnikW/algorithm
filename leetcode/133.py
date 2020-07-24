"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

import collections

class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        clonedNodeDict = {} # 存储着克隆的节点
        queue = collections.deque() # (cloneNode, rawNode) 加入队列的时候node是没克隆邻居的，推出队列的时候（克隆完邻居后）才加上邻居

        cloneRoot = Node(node.val)
        clonedNodeDict[nowNode.val] = cloneRoot
        queue.append((cloneRoot, node))

        while len(queue):
            (clone, raw) = queue.popleft()
            for neighbor in raw.neighbors:
                cloneNode = None
                if neighbor.val not in clonedNodeDict:
                    cloneNode = Node(neighbor.val)
                    clonedNodeDict[neighbor.val] = cloneNode
                    queue.append((cloneNode, neighbor))
                else:
                    cloneNode = clonedNodeDict[neighbor.val]
                clone.neighbors.append(cloneNode)

        return cloneRoot