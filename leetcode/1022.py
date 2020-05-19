# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0

        sum = 0
        def plusAllLeaves(node, parentPath):
            nonlocal sum
            currPath = parentPath + str(node.val)
            if node.left is None and node.right is None:
                sum += int(currPath, 2)
                return
            if node.left is not None:
                plusAllLeaves(node.left, currPath)
            if node.right is not None:
                plusAllLeaves(node.right, currPath)
        
        plusAllLeaves(root, '')
        return sum