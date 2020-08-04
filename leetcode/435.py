def takeFirst(ele):
    return ele[0]

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) < 2:
            return 0

        intervals.sort(key=takeFirst)

        currentStart = intervals[0][0]
        currentEnd = intervals[0][1]
        removeTimes = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start == currentStart:
                removeTimes += 1
                if end < currentEnd:
                    currentEnd = end
            elif start < currentEnd:
                if end <= currentEnd:
                    removeTimes += 1
                    currentStart = start
                    currentEnd = end
                else:
                    removeTimes += 1
            else: # start > currentEnd
                currentStart = start
                currentEnd = end
        
        return removeTimes