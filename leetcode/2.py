class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x >= 0;
        showNotZeroDigit = False;

        intStr = str(abs(x));
        reverseIntStr = '';

        for i in range(len(intStr)-1, -1, -1):
            digit = intStr[i];
            if not showNotZeroDigit and digit == '0':
                # 去除末尾连续的0
                continue;
            else:
                showNotZeroDigit = True;
                reverseIntStr += digit;
        
        # 处理为0的情况
        if len(reverseIntStr) == 0:
            reverseIntStr = '0';

        reverseInt = int(reverseIntStr) if isNegative else -int(reverseIntStr);

        # 检查反转后是否溢出
        if reverseInt > 2147483647 or reverseInt < -2147483648:
            return 0;
        return reverseInt;


def main():
    test1 = 1200; # 21
    test2 = -1200; # -21
    test3 = 12312313123123123123; # 0
    test4 = 0; # 0

    so = Solution();
    for case in (test1, test2, test3, test4):
        print(so.reverse(case));
    

if __name__ == "__main__":
    main()

"""
算法复杂度O(n)

解题关键：
    - 题目明显不难，测试case要写全
    - python3 整型只受制于内存，而不受制于处理器位数，所以可以表示比实际机器位数更大的整数
    - 取边界2的x次方可以用位运算，如31位全是1（即2^31 - 1）可以这样求：1<<31 - 1, 2的n次方即1后面有n个0

一种优化解：
    使用算数运算，
    从原整数origin取出最后一位数x：x = origin % 10
    依次放到结果res的最低位上：res * 10 + x
    将原整数origin减少一位（//代表整除取整）：origin // 10
    直到整除完得到0
"""