# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val < val: # biggerThan current
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        # small than current
        if root.right:
            rightRes = self.insertIntoMaxTree(root.right, val)
            if rightRes.val != root.right.val: # bigger than right child
                root.right = rightRes
        else:
            root.right = TreeNode(val)

        return root