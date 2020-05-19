# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        sortedNodeValues = []

        node = root
        stack = []

        # inorder tree walk, get asc node value
        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            sortedNodeValues.append(node.val)
            node = node.right

        # calc sum of value greater than self
        sumOfGreaterValueOfEveryNode = [0 for i in sortedNodeValues]
        greaterSum = 0
        afterSum = 0
        afterValue = float('inf')
        for i in range(len(sortedNodeValues)-1, -1, -1):
            sumOfGreaterValueOfEveryNode[i] = greaterSum
            afterSum += sortedNodeValues[i]
            if afterValue > sortedNodeValues[i]:
                greaterSum = afterSum
            afterValue = sortedNodeValues[i]

        # update every node val
        walkIndex = 0
        node = root
        stack = []
        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.val += sumOfGreaterValueOfEveryNode[walkIndex]
            walkIndex += 1
            node = node.right

        return root

# 也可以使用反中序遍历（按照右、中、左的顺序遍历），这样就是通过递减的顺序去遍历整棵树
