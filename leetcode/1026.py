# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxDiff = 0
        # post order traversal
        def getMaxAndMinInTree(node):
            nonlocal maxDiff
            # return (min, max)
            if node.left is None and node.right is None:
                return (node.val, node.val)
            leftMin, leftMax = (node.val, node.val) if node.left is None else getMaxAndMinInTree(node.left)
            rightMin, rightMax = (node.val, node.val) if node.right is None else getMaxAndMinInTree(node.right)
            minVal = min(node.val, leftMin, rightMin)
            maxVal = max(node.val, leftMax, rightMax)
            maxDiff = max(
                maxDiff,
                max(abs(node.val - minVal), abs(node.val - maxVal))
            )
            return (minVal, maxVal)

        getMaxAndMinInTree(root)
        return maxDiff