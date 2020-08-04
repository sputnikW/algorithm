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
            prevPoint = header
            biggerTimes = 0
            while True:
                if point.next:
                    prevPoint = point
                    point = point.next
                    nowH, nowK = point.val
                    if nowH >= h:
                        biggerTimes += 1
                    if biggerTimes == k + 1: # 找到第k+1个大于等于h的，插入在它前面
                        newNode = LinkNode([h, k])
                        prevPoint.next = newNode
                        newNode.next = point
                        break

                else: # 找不到，插入到最后（他自己就是比h大的最后一个）
                    point.next = LinkNode([h, k])
                    break
        
        # 遍历链表，获取一个数组
        res = []
        point = header
        while point.next:
            point = point.next
            res.append(point.val)
        
        return res


            
"""
思路：
插入的时候，要求高的值必须基于要求低的值插入，所以要先插入要求低的值
"""