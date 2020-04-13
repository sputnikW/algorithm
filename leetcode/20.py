class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {
            ']': '[',
            '}': '{',
            ')': '('
        };

        stack = [];

        for i in range(len(s)):
            bracket = s[i];
            isCloseBracket = bracket in bracketsMap;
            if isCloseBracket:
                if len(stack) == 0:
                    return False;

                recentOpenBracket = stack.pop();
                if bracketsMap[bracket] != recentOpenBracket:
                    return False;

            else:
                stack.append(bracket);

        return True if len(stack) == 0 else False;

def main():
    testCases = [
        '',
        '()',
        '[{({}){()}}]()',
        ')',
        '(]',
        '({)'
    ];

    so = Solution();

    for case in testCases:
        print(so.isValid(case));

if __name__ == "__main__":
    main();

"""
算法复杂度 O(N)
思考后不难发现解法是看到闭括号时，检查最近的开括号是否匹配得上
所以是有先后顺序的就近配对，自然而然想到了使用栈
"""