# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def isSubPathWithHead(node, targets, head):
            childTargets = []
            targets.append(head)
            for i in range(len(targets)):
                target = targets[i]
                if node.val == target.val:
                    target = target.next
                    if target is None:
                        return True
                    else:
                        childTargets.append(target)
            
            leftRes = False if node.left is None else isSubPathWithHead(node.left, childTargets, head)
            rightRes = False if node.right is None else isSubPathWithHead(node.right, childTargets, head)
            return leftRes or rightRes
        
        return isSubPathWithHead(root, [], head)