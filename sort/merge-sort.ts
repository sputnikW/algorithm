function mergeSort(list: number[]): number[] {
    if (list.length <= 1) {
        return list;
    }

    // 将数组两等分
    // [1,2,3] len // 2 = 1 [1,2,3,4,5,6] len // 2 = 3
    const mid = Math.floor(list.length / 2);
    const leftSubArray = list.slice(0, mid);
    const rightSubArray = list.slice(mid);
    // 对两个子数组分别mergeSort
    const sortedLeft = mergeSort(leftSubArray);
    const sortedRight = mergeSort(rightSubArray);
    // 将两个已经有序的子数组合并
    const fullSortedList: number[] = [];
    let [leftP, rightP] = [0, 0];
    // 直到两个数组为空
    while (leftP !== sortedLeft.length || rightP !== sortedRight.length) {
        // 选择小的；或者如果另一边为空，则直接插入
        if (leftP === sortedLeft.length || sortedLeft[leftP] >= sortedRight[rightP]) {
            fullSortedList.push(sortedRight[rightP]);
            rightP ++;
        }
        else if (rightP === sortedRight.length || sortedLeft[leftP] < sortedRight[rightP]) {
            fullSortedList.push(sortedLeft[leftP])
            leftP ++;
        }
    }
    return fullSortedList;
}