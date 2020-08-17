/**
 * @file 快排
 * - 原地排序
 * - 不稳定排序
 */

function quickSort(list: number[]): number[] {
    if (list.length <= 1) {
        return list;
    }
    // 随机选择一个当前数组中的一个值，将大于它的移到它后面，小于它的移到它前面。
    /** 基准值 */
    const guideVal = list[0];
    /** 基准值当前的索引 */
    let guideIndex = 0;
    /** 已经确定比基准值大的那些值（放在了数组末尾）的第一个值 */
    let biggerTailHeader = list.length;
    while (guideIndex + 1 !== biggerTailHeader) {
        // 直到基准值已经被挪到这样一个位置：右边不再可能有比它还大的值了
        const nextVal = list[guideIndex+1];
        if (nextVal <= guideVal) {
            // 小于它的交换位置
            const tmp = list[guideIndex];
            list[guideIndex] = nextVal;
            list[guideIndex+1] = tmp;
            guideIndex ++;
        }
        else {
            // 大于它的，和biggerTailHeader的前一个交换位置
            const tmp = nextVal;
            list[guideIndex+1] = list[biggerTailHeader-1];
            list[biggerTailHeader-1] = tmp;
            biggerTailHeader --;
        }
    }
    // TODO: 这里开辟了额外的存储空间，实际上可以原地修改，quickSort增加start和end两个参数，分别默认是0和list.length
    // 然后对移动后两边的子数组再进行这个过程
    const leftSide = list.slice(0, guideIndex);
    const rightSide = list.slice(guideIndex+1);

    return [
        ...quickSort(leftSide),
        guideVal,
        ...quickSort(rightSide)
    ];
}