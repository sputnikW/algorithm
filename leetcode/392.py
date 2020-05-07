class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        target = s[0]
        alreadyMatchedTimes = 0
        for i in range(len(t)):
            if t[i] == target:
                # match the target
                alreadyMatchedTimes += 1
                if alreadyMatchedTimes == len(s):
                    # all characters in s has matched
                    return True
                target = s[alreadyMatchedTimes]

        return False

"""
O(N)

follow up:
it will call the func 1 billion times,so each call's time complexity must between O(1) and O(logN)
you should know that the N we talk about is the len of the t, which is nearly 500k
so we cant use beyond way, when we match the s, we should only care about the character in s
so maybe we should pre produce the t before, so we can build a hash link-table, it looks like this:
a -> 1 -> 3 -> 7
b -> 2
c -> 4 -> 6
d -> 5
the node in list table is the position where the letter shown in t
so for each s, we could search letter in s one by one in this hash link-table,
beacause each link-table is sorted,so we can use binanry search,the time cost is LogN,for 500k ,it's about 6
so for each s, the time cost is about 100 * 6,it not to much
"""