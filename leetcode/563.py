# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # post order tree walk traversal
        sum = 0
        def postOrderTraver(node):
            nonlocal sum
            if node.left is None and node.right is None:
                return node.val
            leftSum = 0 if node.left is None else postOrderTraver(node.left)
            rightSum = 0 if node.right is None else postOrderTraver(node.right)
            sum += abs(leftSum - rightSum)
            return leftSum + rightSum + node.val
        postOrderTraver(root)
        return sum