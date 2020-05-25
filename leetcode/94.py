# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        curNode = root
        stack = []
        while stack or curNode is not None:
            while curNode is not None:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()
            nodes.append(curNode.val)
            curNode = curNode.right
        
        return nodes