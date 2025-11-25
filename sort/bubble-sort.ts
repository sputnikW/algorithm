/**
 * @file 冒泡排序
 * - 稳定排序
 * - 原地排序
 * - 时间复杂度 O(n²)
 */

/**
 * 基础冒泡排序
 * @param list 待排序数组
 * @returns 已排序数组
 */
function bubbleSort(list: number[]): number[] {
    if (list.length <= 1) {
        return list;
    }

    // 创建副本以避免修改原数组
    const arr = [...list];
    const n = arr.length;

    // 外层循环：需要进行 n-1 轮比较
    for (let i = 0; i < n - 1; i++) {
        // 内层循环：每轮将最大值"冒泡"到末尾
        // 每完成一轮,末尾就有一个元素已排好序,所以范围是 n-1-i
        for (let j = 0; j < n - 1 - i; j++) {
            // 比较相邻元素,如果前者大于后者则交换
            if (arr[j] > arr[j + 1]) {
                const temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    return arr;
}

/**
 * 优化的冒泡排序(带提前终止)
 * @param list 待排序数组
 * @returns 已排序数组
 */
function bubbleSortOptimized(list: number[]): number[] {
    if (list.length <= 1) {
        return list;
    }

    // 创建副本以避免修改原数组
    const arr = [...list];
    const n = arr.length;

    // 外层循环：需要进行 n-1 轮比较
    for (let i = 0; i < n - 1; i++) {
        /** 标记本轮是否发生交换 */
        let hasSwapped = false;

        // 内层循环：每轮将最大值"冒泡"到末尾
        for (let j = 0; j < n - 1 - i; j++) {
            // 比较相邻元素,如果前者大于后者则交换
            if (arr[j] > arr[j + 1]) {
                const temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                hasSwapped = true;
            }
        }

        // 如果本轮没有发生任何交换,说明数组已经有序,可以提前结束
        if (!hasSwapped) {
            break;
        }
    }

    return arr;
}

// 测试用例
// const unsorted = [64, 34, 25, 12, 22, 11, 90];
// console.log('原数组:', unsorted);
// console.log('基础冒泡排序:', bubbleSort(unsorted));
// console.log('优化冒泡排序:', bubbleSortOptimized(unsorted));
//
// const nearlySorted = [1, 2, 3, 5, 4];
// console.log('近乎有序数组:', nearlySorted);
// console.log('优化冒泡排序(提前终止):', bubbleSortOptimized(nearlySorted));
