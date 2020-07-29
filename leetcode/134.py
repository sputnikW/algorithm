class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalRemain = 0
        remainFromStart = 0
        start = None
        for i in range(len(gas)):
            remain = gas[i] - cost[i] # remain when cross the station
            remainFromStart += remain
            if remainFromStart < 0:
                start = None
                remainFromStart = 0
            elif start is None:
                start = i
            totalRemain += remain
        
        return start if totalRemain >= 0 else -1