# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        diameter = 0
        def getTreeHeight(node):
            nonlocal diameter
            if node.left is None and node.right is None:
                return 0
            leftHeight = 0 if node.left is None else getTreeHeight(node.left) + 1
            rightHeight = 0 if node.right is None else getTreeHeight(node.right) + 1
            diameter = max(leftHeight + rightHeight, diameter)
            return max(leftHeight, rightHeight)
        getTreeHeight(root)

        return diameter