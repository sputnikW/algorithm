# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def findMaxNode(node):
            if node.right != None:
                return findMaxNode(node.right)
            else:
                return node.val

        def findMinNode(node):
            if node.left != None:
                return findMinNode(node.left)
            else:
                return node.val
        
        minDiff = float('inf')
        def findNodeClosestChild(node):
            if node.left == None and node.right == None:
                return

            nonlocal minDiff
            maxOfLeftTree = -float('inf') if node.left == None else findMaxNode(node.left)
            minOfRightTree = float('inf') if node.right == None else findMinNode(node.right)
            minDiff = min(minDiff, node.val - maxOfLeftTree, minOfRightTree - node.val)
            if node.left != None:
                findNodeClosestChild(node.left)
            if node.right != None:
                findNodeClosestChild(node.right)
        findNodeClosestChild(root)

        return minDiff

# solution2: use BST 's inorder tree walk is asc order
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        minDiff = float('inf')
        prevNodeVal = None

        node = root
        stack = []
        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prevNodeVal is not None:
                minDiff = min(node.val - prevNodeVal, minDiff)
            prevNodeVal = node.val

            node = node.right

        return minDiff