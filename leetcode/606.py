# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ''

        # return the required string
        def preOrderTraver(node):
            if node.left is None and node.right is None:
                return str(node.val)
            leftStr = '()' if node.left is None else '(' + preOrderTraver(node.left) + ')'
            rightStr = '' if node.right is None else '(' + preOrderTraver(node.right) + ')'
            return str(node.val) + leftStr + rightStr
        return preOrderTraver(t)