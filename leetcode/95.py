# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        dp = [
            [
                None for j in range(n+1)
            ] for i in range(n+1)
        ]

        for i in range(1, n+1): # right edge
            for j in range(i, 0, -1): # left edge
                # [1,1]
                # [2,2] [1,2]
                # [3,3] [2,3] [1,3]
                res = [] # res of dp[j, i]
                if j == i:
                    res = [TreeNode(j)]
                else:
                    # eg: i = 3 j = 1
                    for k in range(j, i+1):
                        lefts = [None] if k == j else dp[j][k-1]
                        rights = [None] if k == i else dp[k+1][i]
                        for left in lefts:
                            for right in rights:
                                root = TreeNode(k)
                                root.left = left
                                root.right = right
                                res.append(root)
                dp[j][i] = res
        
        return dp[1][n]