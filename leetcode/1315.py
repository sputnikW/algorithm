# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum = 0
        def preOrderTraver(node, grandPaVal, parentVal):
            nonlocal sum
            if node is None:
                return
            if grandPaVal is not None and grandPaVal % 2 == 0:
                sum += node.val
            preOrderTraver(node.left, parentVal, node.val)
            preOrderTraver(node.right, parentVal, node.val)
        
        preOrderTraver(root, None, None)
        return sum