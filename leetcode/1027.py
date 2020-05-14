class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        maxLen = 0
        prevResults = [{} for i in range(len(A))]

        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]

                lenOfSequence = 2 # defalut, there are 2 elements in sequence
                if diff in prevResults[j]: # check j
                    lenOfSequence = prevResults[j][diff] + 1

                if diff in prevResults[i]: # if already meet some number has same diff, chose the longest one
                    prevResults[i][diff] = max(lenOfSequence, prevResults[i][diff])
                else:
                    prevResults[i][diff] = lenOfSequence

                maxLen = max(maxLen, prevResults[i][diff])
        
        return maxLen