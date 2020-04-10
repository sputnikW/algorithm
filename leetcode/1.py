class Solution:
    def twoSum(self, nums, target):
        result = [];
        numsLen = len(nums);

        for i in range(numsLen):
            num = nums[i];
            if i == numsLen - 1:
                return [];
            else:
                restList = nums[i+1:];
                minus = target - num;
                if minus in restList:
                    return [i, restList.index(minus) + i + 1]
                # for x in range(len(restList)):
                #     restNum = restList[x];
                #     if num + restNum == target:
                #         return [i, x + i + 1];

def main():
    nums = [3,2,4];
    target = 6;

    sol = Solution();

    res = sol.twoSum(nums, target);
    print(res);

if __name__ == '__main__':
    main()
    

TODO:
"""
解法基本类似：
遍历数组，对每一个值，搜索是否有与之契合的另外一个值

关键点有两个：
- 搜索的方式有多种：
    - 遍历搜索
    - 使用py内置的 in 关键字（就是线性搜索），再使用List的index方法获取位置（这个是遍历吗？）
    - 使用hashMap（其实也就是python的dict类型）存储查找过的数字，key是数字，value是数组的索引（因为对象是对key做hash去存储值，所以判断一个key是否在hashMap中只需要O(1)的算法复杂度，整个算法就是O(n)）
- 搜索另外一个值的时候，可以在数组的剩余部分搜索，没有必要搜索整个数组
"""