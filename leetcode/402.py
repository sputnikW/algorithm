class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0 or len(num) == 0:
            return num

        stack = [num[0]]
        i = 1
        while k > 0:
            if i < len(num):
                if stack:
                    subling = stack.pop()
                    if num[i] < subling:
                        k -= 1
                    else:
                        stack.append(subling)
                        if num[i] > '0':
                            stack.append(num[i])
                        i += 1
                else:
                    if num[i] > '0':
                        stack.append(num[i])
                    i += 1
            else:
                # 说明一直检查到最后一位了，直接从末尾把剩下的给删除(注意k>STACK时的情况)
                if stack:
                    stack.pop()
                    k -= 1
                else:
                    break

        prefix = ''.join(stack)
        newNum = prefix + num[i:] if i < len(num) else prefix
        # 有可能因为k的原因退出了，所以可能有多余的0在前面，去掉leading zero
        zeroIndex = 0
        for j in range(len(newNum)):
            if newNum[j] == '0':
                zeroIndex = j + 1
            else:
                break
        return newNum[zeroIndex:]
    
def main():
    so = Solution()
    so.removeKdigits("10200", 1)

if __name__ == "__main__":
    main()