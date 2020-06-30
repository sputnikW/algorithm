# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
            return False
        pairMap = {}
        # insert [left, right] into map like: n: [left, right]
        def getVal(node):
            return None if node is None else node.val

        def insertIntoMap(node):
            nonlocal pairMap
            if node is None:
                return
            pairMap[node.val] = [getVal(node.left), getVal(node.right)]
            insertIntoMap(node.left)
            insertIntoMap(node.right)
        insertIntoMap(root1)

        def checkMap(node):
            nonlocal pairMap
            if node is None:
                # care for that root is None, where return True
                return True
            # check child
            if node.val not in pairMap:
                return False
            child = pairMap[node.val]
            if (getVal(node.left) == child[0] and getVal(node.right) == child[1]) or (getVal(node.left) == child[1] and getVal(node.right) == child[0]):
                return checkMap(node.left) and checkMap(node.right)
            else:
                return False

        return checkMap(root2)

def main():
    root1 = TreeNode(0)
    root1.left = TreeNode(3)
    root1.right = TreeNode(1)
    root1.right.right = TreeNode(2)

    root2 = TreeNode(0)
    root2.left = TreeNode(3)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(2)

    so = Solution()
    so.flipEquiv(root1, root2)


if __name__ == "__main__":
    main()

"""
注意可能存在的非法输入的情况，要避免程序崩溃
"""