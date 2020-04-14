class Solution:
    def removeElement(self, nums, val) -> int:
        isEnd = len(nums) == 0; # will skip empty list
        point = 0;

        while not isEnd:
            isEnd = point == len(nums) - 1;
            if nums[point] == val:
                nums.pop(point);
            else:
                point += 1;

        return len(nums);

def main():
    testCases1 = [];
    testCases2 = [1];
    testCases3 = [3,3,4,4,2,4,5,5,7,2];

    so = Solution();
    so.removeElement(testCases1, 1);
    so.removeElement(testCases2, 2);
    so.removeElement(testCases3, 2);

    print(testCases1);
    print(testCases2);
    print(testCases3);

if __name__ == "__main__":
    main();

"""
算法复杂度O(N)
这题有空间复杂度的要求，不能创建额外的数组，要求在传入的数组上直接操作。
没啥难得，这里主要用了一个指针，记录当前要检查的元素的位置。
如果是不修改原数组的长度，则用两个指针，把不符合要求的值通通交换到数组的末尾
"""