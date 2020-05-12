class Solution:
    def clipIsIncludeInOtherClip(self, clip, otherClip):
        return otherClip[0] <= clip[0] and otherClip[1] >= clip[1]

    def takeStart(self, ele):
        return ele[0]

    def videoStitching(self, clips, T):
        # remove all bad clip which can be replaced by other
        needRemoveIndex = [0 for i in range(len(clips))]
        for i in range(len(clips)):
            if (needRemoveIndex[i] == 1):
                continue
            for j in range(i+1, len(clips)):
                if (needRemoveIndex[i] == 1):
                    continue
                if self.clipIsIncludeInOtherClip(clips[i], clips[j]):
                    needRemoveIndex[i] = 1
                elif self.clipIsIncludeInOtherClip(clips[j], clips[i]):
                    needRemoveIndex[j] = 1
        importantClips = []
        for i in range(len(needRemoveIndex)):
            if needRemoveIndex[i] == 0:
                importantClips.append(clips[i])
        
        # sort by the clip's start asc
        importantClips.sort(key=self.takeStart)

        # start dp process
        # edge case
        if T == 0:
            return 0

        # init dp(0) dp(1)
        neededClips = 0
        end = 0
        prevIndex, currIndex = -1, -1 

        if importantClips[0][0] > 0:
            return -1
        prevIndex = 0
        end = importantClips[0][1]
        neededClips += 1
        if end >= T:
            return neededClips

        if len(importantClips) == 1:
            return -1
        
        if importantClips[1][0] > importantClips[0][1]:
            return -1
        currIndex = 1
        end = importantClips[1][1]
        neededClips += 1
        if end >= T:
            return neededClips

        # start dp
        for i in range(2, len(importantClips)):
            curClip = importantClips[i]
            if curClip[0] > importantClips[currIndex][1]:
                return -1
            if curClip[0] > importantClips[prevIndex][1]:
                neededClips += 1
                prevIndex = currIndex
                currIndex = i
            else: # currIndex clip is not necessary
                currIndex = i
            end = curClip[1]
            if end >= T:
                return neededClips

        return -1

def main():
    so = Solution()

    print(so.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))

if __name__ == "__main__":
    main()

"""
T=O(N^2)
关键
- 乱序的情况下不便于找最优解，所以要排一下序
- 这里可以不做N^2的去除无效片段的操作，排完序后有一种贪心的方式，可以保证每次选择的都是最优解，能将复杂度减少到NLogN
"""