class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False;
        elif 0 <= x < 10:
            return True;
        else:
            intStr = str(x);
            pointForward = 0;
            pointBackword = len(intStr) - 1;
            while pointBackword > pointForward:
                if intStr[pointForward] != intStr[pointBackword]:
                    return False;
                pointForward += 1;
                pointBackword -= 1;
            return True;

def main():
    testCases = [121, -121, 555, 1234321, 1010, 1001, 0];

    so = Solution();
    for case in testCases:
        print(so.isPalindrome(case));
    

if __name__ == "__main__":
    main();

"""
思路比较简单，从前往后和从后往前比较对应位置的数字是否相等。

方式的不同可能在于如果取前面x位和后面x位以进行比较，有这些方法：
    - 转成字符串
    - 转成数组（需要注意数组的pop操作是O(N)的，因为需要逐个移动数组中元素的位置，所以此操作比较慢）
    - 看题解有人有一些奇技淫巧，比如直接对数字做运算，%10取的是最后一位，// 10 * 数值位数取的是第一位的数组（数值的位数用log(x, 10)来计算...）

还有其他一些方法，如算出数字后半部分（或前半部分）的反转数（可以参考反转数字那一题 #2），然后直接对数值进行比较。
"""