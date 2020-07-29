class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalRemain = 0
        remainFromStart = 0
        start = None
        for i in range(len(gas)):
            remain = gas[i] - cost[i] # remain when cross the station
            if remain >= 0 and start is None: # first increase index
                start = i
                remainFromStart += remain
            elif remain < 0 and remainFromStart + remain < 0: # reset start when decrease under 0
                start = None
            totalRemain += remain
        
        return start if totalRemain >= 0 else -1