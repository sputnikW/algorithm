class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        neddleLen = len(needle)
        shouldLookLen = len(haystack) - neddleLen + 1

        if shouldLookLen < 0:
            return -1

        for i in range(shouldLookLen):
            sameLenSubStrFromI = haystack[i:i + neddleLen]
            if sameLenSubStrFromI == needle:
                return i

        return -1

def main():
    testCaseH = [
        'hello',
        '',
        'apple',
        'this is what we know'
    ]

    testCaseN = [
        'll',
        'll',
        'apples',
        'we'
    ]

    so = Solution()
    for i in range(len(testCaseH)):
        print(so.strStr(testCaseH[i], testCaseN[i]))


if __name__ == "__main__":
    main()

# O(N)