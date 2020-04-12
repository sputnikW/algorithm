import sys;

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        minLen = sys.maxsize if len(strs) else 0;
        for str in strs:
            strLen = len(str);
            if strLen < minLen:
                minLen = strLen;

        commonPrefix = '';
        for i in range(minLen):
            currentChar = strs[0][i];
            for str in strs:
                if str[i] != currentChar:
                    return commonPrefix;
            commonPrefix += currentChar;

        return commonPrefix;

def main():
    testCases = [
        ['abcdef', 'abcdf', 'abr'], # ab
        ['asdasd', 'asd', ''], # ''
        ['asd', 'dgf', 'sdf'], # ''
        [], # ''
    ];

    so = Solution();
    for case in testCases:
        print(so.longestCommonPrefix(case));


if __name__ == "__main__":
    main();

"""
算法复杂度 O(N * M) N是strs长度，M是公共前缀的长度
不管怎么说，求公共子串，都是要遍历所有数组中的字符串的，N的算法复杂度跑不了
而对比每个字符串中的字符也是跑不掉的，最起码，公共前缀里的那些字符，都要对比一遍才能得出
所以这应该是最小的复杂度了。
"""