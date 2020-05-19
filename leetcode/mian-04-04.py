# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return True if self.getHeightIfBalance(root) != -1 else False
    
    def getHeightIfBalance(self, node):
        # return height if node is balanced, else return -1
        if node == None:
            return 0
        elif node.left == None and node.right == None:
            return 1
        else:
            left = self.getHeightIfBalance(node.left)
            if left == -1:
                return -1
            right = self.getHeightIfBalance(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1