# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None:
            return True
        if s is None:
            return False

        # post order traver the target subtree
        subTree = []
        def postOrderTarver(node):
            nonlocal subTree
            if node.left is None and node.right is None:
                subTree.append(node.val)
                return
            if node.left is not None:
                postOrderTarver(node.left)
            else:
                subTree.append(None)
            if node.right is not None:
                postOrderTarver(node.right)
            else:
                subTree.append(None)
            subTree.append(node.val)
        postOrderTarver(t)

        # return the postOrder tree node

        def sameArrayCheck(array1, array2):
            if len(array1) != len(array2):
                return False
            for i in range(len(array1)):
                if array1[i] != array2[i]:
                    return False
            return True

        # return None if Find,otherwise return List
        def getPostOrderTreeNode(node):
            nonlocal subTree
            if node.left is None and node.right is None:
                if sameArrayCheck([node.val], subTree):
                    return None
                return [node.val]

            leftNodeList = [None] if node.left is None else getPostOrderTreeNode(node.left)
            if leftNodeList is None:
                return None

            rightNodeList = [None] if node.right is None else getPostOrderTreeNode(node.right)
            if rightNodeList is None:
                return None
            currList = leftNodeList + rightNodeList + [node.val]
            # check if is same to subTree
            if sameArrayCheck(currList, subTree):
                return None

            return currList
        
        res = getPostOrderTreeNode(s)
        return True if res is None else False