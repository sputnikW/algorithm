# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        # from 1 to every posible n less then N, composite every posible pair
        res = []
        for i in range(1, N, 2):
            leftTrees = self.allPossibleFBT(i)
            rightTrees = self.allPossibleFBT(N - i - 1);
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    root = TreeNode(0)
                    root.left = leftTree
                    root.right = rightTree
                    res.append(root)
        return res
