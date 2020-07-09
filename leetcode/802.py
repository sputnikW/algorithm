class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        nodeColors = {}
        for i in range(len(graph)):
            nodeColors[i] = 'white'

        def dfs(node): # return if is safe
            if nodeColors[node] != 'white':
                return nodeColors[node] == 'black'
            
            nodeColors[node] = 'gary'
            for vertex in graph[node]:
                if nodeColors[vertex] == 'gary':
                    return False
                elif nodeColors[vertex] == 'black':
                    continue
                elif nodeColors[vertex] == 'white':
                    res = dfs(vertex)
                    if not res:
                        return False
                    else:
                        continue
            
            nodeColors[node] = 'black'
            return True

        return filter(dfs, range(len(graph)))