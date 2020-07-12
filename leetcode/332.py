class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def findItinerary(self, tickets):
        # 如何快速找到节点最小的后置节点 O-E/每次 * N次 -> 转成邻接"链表"(用deque简化)，往列表中插入的时候有序插入（E次 * 每次E/N）
        graph = {}
        for ticket in tickets:
            [start, end] = ticket
            if start not in graph:
                graph[start] = []
            graph[start].append(end)
        
        for start in graph:
            graph[start].sort()
            import collections
            graph[start] = collections.deque(graph[start])

        # 先构造一颗树，由于是知道起始点的，所以直接从起始点开始
        # 借助栈，访问顶的节点，如果不剩下边了，则结束；如果没有出度，则出栈，再判断下一轮；如果有出度，则出度节点进栈
        root = TreeNode('JFK')
        stack = [root];
        remainTicketLen = len(tickets)
        while remainTicketLen:
            currNode = stack[-1]
            if currNode.val not in graph or len(graph[currNode.val]) == 0:
                stack.pop();
            else:
                remainTicketLen -= 1
                # 把邻接链表中第一个节点取出来
                firstNode = graph[currNode.val].popleft()

                firstTreeNode = TreeNode(firstNode)
                if currNode.left is None:
                    currNode.left = firstTreeNode
                else:
                    currNode.right = firstTreeNode
                stack.append(firstTreeNode)

        # 后序遍历这颗树，然后反转
        postOrder = []
        def postOrderTraversal(node):
            if node is None:
                return
            postOrderTraversal(node.left)
            postOrderTraversal(node.right)
            postOrder.append(node.val)
        
        postOrderTraversal(root)

        postOrder.reverse()
        return postOrder

def main():
    so = Solution()
    so.findItinerary([["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]])

if __name__ == '__main__':
    main()

"""
抽象描述：
在一个有向图中，从一个源，遍历所有节点的路径，可能会有环（欧拉路径问题） -> 构造二叉树表示拓扑关系

思路：
因为访问某一个节点必须先访问前置节点，自然想到了拓扑排序
然而拓扑排序是对于有向无环图来说的，而这里是有环图，所以排序后的树中，就存在“相同”的节点了
另外为了找到路径，如何在树里找到路径呢？就是遍历
遍历中一定是先左后右，所以在生成树的时候小的放左边，优先走左边
因为首先我们树里是有相同节点的，也就是说可能从树的某一个后代的节点，直接跳到其祖先上的相同节点的某个儿子上
要实现这样的顺序——从一个后代、跳到另一个后代——只有两种可能，先序或者后序，因为要先访问父节点，所以如果是后序的话，一定是后序完再倒过来的

思考典型case：访问起点的一条边，到了一个死路，还没访问完，该怎么办？只能回溯到之前的“岔路”，然后走另一条路试试（往右）
也就是说但凡有右子树，就应该先走右子树，因为左路是不通的，那说明遍历一定是要反过来的，也就是反过来的后序遍历
"""
