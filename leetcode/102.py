# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        result = []
        def pushIntoResult(val, level):
            nonlocal result
            if len(result) <= level:
                result.append([val])
            else:
                result[level].append(val)

        def preOrderTraversal(node, level):
            nonlocal result
            if node is None:
                return
            # handle node
            pushIntoResult(node.val, level)

            # left child
            preOrderTraversal(node.left, level + 1)

            # right child
            preOrderTraversal(node.right, level + 1)

        preOrderTraversal(root, 0)
        return result
            


"""
T=O(N) S=O(N)
这题还可以用BFS的方式进行遍历，即用一个队列维护遍历中的节点。
额外需要考虑的就是在遍历的时候要额外分一下层
"""