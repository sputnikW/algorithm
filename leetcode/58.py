class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        showAlphabet = False

        for i in range(len(s) - 1, -1, -1):
            if (not showAlphabet) and s[i] == ' ':
                continue

            if s[i] == ' ':
                break
            else:
                count += 1
                showAlphabet = True
        
        return count

def main():
    testCases = [
        'hello world',
        '',
        'test',
        'test ',
        'hello world is very  better'
    ]

    so = Solution()
    for case in testCases:
        print(so.lengthOfLastWord(case))

if __name__ == "__main__":
    main()

"""
O(N)
需要注意的是题目的描述，对最后一个word的定义，'test   '这种最后一个word依然是'test'
"""