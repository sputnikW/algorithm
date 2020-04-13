# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x;
        self.next = None;

class Solution:
    def mergeTwoLists(self, l1, l2) -> ListNode:
        header = ListNode(-1);
        tailOfRes = header;

        while l1 or l2:
            # when any list is empty, put the other to the tail of result list
            if l1 is None:
                tailOfRes.next = l2;
                break;
            if l2 is None:
                tailOfRes.next = l1;
                break;

            if l1.val > l2.val:
                tailOfRes.next = l2;
                tailOfRes = tailOfRes.next;
                l2 = l2.next;
            else:
                tailOfRes.next = l1;
                tailOfRes = tailOfRes.next;
                l1 = l1.next;

        return header.next;

def main():
    l1 = ListNode(1);
    l1.next = ListNode(2);
    l1.next.next = ListNode(3);

    l2 = ListNode(1);
    l2.next = ListNode(3);
    l2.next = ListNode(4);

    so = Solution();
    newList = so.mergeTwoLists(l1, l2);
    while newList:
        print(newList.val);
        newList = newList.next;
    
    # testList2 = so.mergeTwoLists(l1, None);
    # while testList2:
    #     print(testList2.val);
    #     testList2 = testList2.next;

if __name__ == "__main__":
    main();


"""
算法其实很简单，最坏情况是O(N + M)的算法复杂度
需要注意的是，为了能够像处理列表中其他节点一样，处理链表中第一个节点，可以在表头增加一个哨兵节点header。
当前算法有一个缺点，就是会修改输入不过貌似对链表进行不修改的操作也比较麻烦？
"""