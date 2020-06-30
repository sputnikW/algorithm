# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # iterate with some side effect
        duplicateSubTrees = []
        subTreeMap = {} # treeStr: times
        def getTreeStr(node):
            nonlocal duplicateSubTrees
            nonlocal subTreeMap

            if node is None:
                return '#'
            
            leftTreeStr = getTreeStr(node.left)
            rightTreeStr = getTreeStr(node.right)
            treeStr = str(node.val) + ',' + leftTreeStr + ',' + rightTreeStr

            if treeStr in subTreeMap:
                if subTreeMap[treeStr] == 1:
                    duplicateSubTrees.append(node)
                    subTreeMap[treeStr] = 2
            else:
                subTreeMap[treeStr] = 1
            
            return treeStr

        getTreeStr(root)
        return duplicateSubTrees
