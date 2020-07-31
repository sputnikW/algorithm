def takeSecond(ele):
    return ele[1]

class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=takeSecond)

        header = LinkNode(None)
        for person in people:
            h, k = person
            point = header
            while point.next:
                # 找到第k+1个大于等于h的，插入在它前面
                # 如果找不到，插入到最后（他自己就是比h大的最后一个）


            
"""
思路：
插入的时候，要求高的值必须基于要求低的值插入，所以要先插入要求低的值
"""