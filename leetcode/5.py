# 中心拓展的方式
# manacher algorithm

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalinLen = 0
        longestPalinStr = ''
        # use cur item as center
        for i in range(len(s)):
            le, ri = i - 1, i + 1
            palinLen, palinStr = 1, s[i]
            while le >= 0 and ri < len(s):
                if s[le] == s[ri]:
                    palinLen += 2
                    palinStr = s[le] + palinStr + s[ri]
                    le -= 1
                    ri += 1
                else:
                    break
            if palinLen > maxPalinLen:
                maxPalinLen = palinLen
                longestPalinStr = palinStr
        # use cur item and right item as center
        for i in range(len(s)-1):
            le, ri = i, i + 1
            palinLen, palinStr = 0, ''
            while le >= 0 and ri < len(s):
                if s[le] == s[ri]:
                    palinLen += 2
                    palinStr = s[le] + palinStr + s[ri]
                    le -= 1
                    ri += 1
                else:
                    break
            if palinLen > maxPalinLen:
                maxPalinLen = palinLen
                longestPalinStr = palinStr
        return longestPalinStr
                