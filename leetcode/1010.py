class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairsCount = 0
        timeLen = len(time)

        existedTime = {}
        for i in range(timeLen):
            current = time[i]
            for duration, existedTimes in existedTime.items():
                if (duration + current) % 60 == 0:
                    pairsCount += existedTimes
            existedTime[current] = existedTime[current] + 1 if current in existedTime else 1

        return pairsCount

"""
O(N * M) M是time的值的个数
这题的关键在于，如何在当前值和其他值比较时，少比较一些，这里的思路是大小相同的值视为同一个值，用一个字典记录这种值出现的次数
不过还可以进一步优化：即将所有对60求余数相同的值都视为同一个值，这样能减小M
"""