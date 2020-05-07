class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        if len(nums) > 0:
            self.sums.append(nums[0])
            for i in range(1, len(nums)):
                self.sums.append(self.sums[i-1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        sums = self.sums
        if len(sums) == 0:
            return 0

        return sums[j] if i == 0 else sums[j] - sums[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

"""
O（N+M），M为请求次数
由于调用sumRange的次数可能很多，所以自然希望sumRange的复杂度尽可能小，那基本可以确定要O（1）的复杂度
那就只能做预计算了，最暴力的方式，是把所有可能的组合都算出来，但是这里情况比较特殊
并不需要算所有可能的起点和终点的组合，只需要算到每一点的和就可以通过数学式算出来
"""