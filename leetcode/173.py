# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = []
        self.curPos = 0
        # todo: in-order traversal the root
        def inOrderTraversal(node):
            if node is None:
                return
            inOrderTraversal(node.left)
            self.queue.append(node.val)
            inOrderTraversal(node.right)
        inOrderTraversal(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.queue[self.curPos]
        self.curPos += 1
        return res


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.curPos < len(self.queue) else False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
