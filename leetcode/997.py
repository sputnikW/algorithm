class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # traversal trust, find a label that from times = 0, to times = N
        dontTrustOthers = {}
        beTrustedTimesMap = {}
        for i in range(1, N + 1): # N
            dontTrustOthers[i] = None
            beTrustedTimesMap[i] = 0
        for trustRelation in trust: # M
            if trustRelation[0] in dontTrustOthers:
                del dontTrustOthers[trustRelation[0]]
            beTrustedTimesMap[trustRelation[1]] += 1

        for label in dontTrustOthers.keys(): # N
            if beTrustedTimesMap[label] == N - 1:
                return label
        
        return -1

"""
标准的解法可能是构造一个节点列表，每个节点中存储节点的出度和入度
然后查找入度为N-1，出度为0的节点
"""