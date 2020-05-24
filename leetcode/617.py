# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        # trans tree to a dict, which key is path('l'->left 'r'->right '1'->root),value is the node value
        mergedTree = {}
        
        # preorder traver
        def transTreeToMergedDict(node, path):
            nonlocal mergedTree
            if node is None:
                return
            mergedTree[path] = node.val if path not in mergedTree else mergedTree[path] + node.val
            transTreeToMergedDict(node.left, path+'l')
            transTreeToMergedDict(node.right, path+'r')
        
        transTreeToMergedDict(t1, '1')
        transTreeToMergedDict(t2, '1')

        # build the tree from dict
        mergedRootNode = TreeNode(None)
        nodeAndPathStack = [(mergedRootNode, '1')]
        while nodeAndPathStack:
            node, path = nodeAndPathStack.pop()
            node.val = mergedTree[path]
            if path + 'l' in mergedTree:
                leftChild = TreeNode(None)
                node.left = leftChild
                nodeAndPathStack.append((leftChild, path+'l'))
            if path + 'r' in mergedTree:
                rightChild = TreeNode(None)
                node.right = rightChild
                nodeAndPathStack.append((rightChild, path+'r'))
        
        return mergedRootNode

"""
O(N)
此题有一个特点，即树或者链表这种数据结构，有时是不需要处理所有结点的，因为节点和节点之间是通过指针进行连接
"""