class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        g.reverse()
        s.sort()
        s.reverse()
        res = 0

        g_p, s_p = 0, 0
        while s_p < len(s) and g_p < len(g):
            # 检查当前的size是否满足当前的greed
            if s[s_p] >= g[g_p]:
                res += 1
                s_p += 1
                g_p += 1
            else:
                g_p += 1

        return res