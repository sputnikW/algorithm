class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumberAsc = ['I', 'V', 'X', 'L', 'C', 'D', 'M'];
        numberMapForRoman = [1, 5, 10, 50, 100, 500, 1000];

        lenOfRomanNumber = len(s);
        integer = 0;

        # 从前往后遍历，如果当前字符大于或等于后面的字符，则累加，否则则减去当前字符
        for i in range(lenOfRomanNumber):
            romanNumeral = s[i];
            isLastNumber = i == lenOfRomanNumber - 1;

            indexOfRoman = romanNumberAsc.index(romanNumeral);
            valueOfRoman = numberMapForRoman[indexOfRoman];

            if isLastNumber:
                integer += valueOfRoman;
                break;

            nextRoman = s[i + 1];
            indexOfNextRoman = romanNumberAsc.index(nextRoman);
            nextIsBigger = indexOfNextRoman > indexOfRoman;
            if nextIsBigger:
                integer -= valueOfRoman;
            else:
                integer += valueOfRoman;

        return integer;

def main():
    testCases = [
        'I',
        'III',
        'IV',
        'V',
        'VI',
        'IX',
        'XXVII',
        'MMDCLXVI'
    ];

    expects = [
        1,
        3,
        4,
        5,
        6,
        9,
        27,
        2666
    ];

    so = Solution();

    for case in testCases:
        isPass = so.romanToInt(case) == expects[testCases.index(case)];
        print(isPass);

if __name__ == "__main__":
    main();

"""
没啥好说的，规律很容易找到，如前文的唯一一条注释所说, 算法复杂度是O(N*个位数)级别的。

唯一需要注意的就是如何存储罗马数字和阿拉伯数字的对应关系：
    - 我使用的是两个对应的数组，因为数组中元素有限，所以查找不是很费时，但有更好的方式
    - 使用哈希表（字典），存储罗马数字和阿拉伯数字的对应关系，取值的算法复杂度是O(1)，肯定要更快些，并且存为一个字典，肯定比存两个数组要可维护的多。
"""