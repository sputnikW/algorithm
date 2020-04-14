class Solution:
    def removeDuplicates(self, nums) -> int:
        isEnd = len(nums) <= 1; # will skip empty list or only one element list
        point = 1;

        while not isEnd:
            isEnd = point == len(nums) - 1;
            if nums[point - 1] == nums[point]:
                nums.pop(point);
            else:
                point += 1;

        return len(nums);

def main():
    testCases1 = [];
    testCases2 = [1];
    testCases3 = [1,3,3,4,4,4,4,5,5,7];

    so = Solution();
    so.removeDuplicates(testCases1);
    so.removeDuplicates(testCases2);
    so.removeDuplicates(testCases3);

    print(testCases1);
    print(testCases2);
    print(testCases3);

if __name__ == "__main__":
    main();

"""
由于pop是O(N)的操作，最坏情况是所有元素都要移除，算法复杂度是O(NlogN)，最好情况是O(N)
这题有空间复杂度的要求，不能创建额外的数组，要求在传入的数组上直接操作。
没啥难得，这里主要用了一个指针，记录当前要去比较的元素的位置。
也可以用双指针，复杂度更佳，更稳定
"""