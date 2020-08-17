type CompareFunc<T> = (parent: T, child: T) => boolean;

class Heap<T> {
    heap: T[] = [];
    cmp: CompareFunc<T>;

    private getParentIndex(index: number) {
        if (index === 0) {
            return null;
        }
        return Math.floor((index-1) / 2);
    }
    
    private getLeftChildIndex(index: number) {
        const childIndex = index * 2 + 1;
        return childIndex < this.heap.length ? childIndex : null;
    }
    
    private getRightChildIndex(index: number) {
        const childIndex = index * 2 + 2;
        return childIndex < this.heap.length ? childIndex : null;
    }

    /**
     * 从一个节点开始，只要它和它的child不满足堆的性质，则和对应的child进行交换，直到成为叶子节点或者满足性质
     * @param index 要sift down的节点
     */
    private siftDown(index: number) {
        const leftChildIndex = this.getLeftChildIndex(index);
        const rightChildIndex = this.getRightChildIndex(index);
        // 如果是叶子节点，直接return
        if (leftChildIndex === null && rightChildIndex === null) {
            return;
        }
        let theBiggerChild: T;
        let biggerSideIndex: number;
        if (rightChildIndex === null || this.cmp(this.heap[leftChildIndex], this.heap[rightChildIndex])) {
            // 如果右child为空或者右child小于左child
            theBiggerChild = this.heap[leftChildIndex];
            biggerSideIndex = leftChildIndex;
        }
        else {
            theBiggerChild = this.heap[rightChildIndex];
            biggerSideIndex = rightChildIndex;
        }
        // 否则则和child中大的那个进行比较
        if (this.cmp(this.heap[index], theBiggerChild)) {
            // 如果大于它，则return
            return;
        }
        else {
            // 否则则交换，然后继续sift down
            const tmp = this.heap[index];
            this.heap[index] = theBiggerChild;
            this.heap[biggerSideIndex] = tmp;
            this.siftDown(biggerSideIndex);
        }
    }

    /** 从当前节点，和父亲节点比较，如果不满足堆的条件，则交换，直到满足或到达顶端 */
    private siftUp(index: number) {
        const parentIndex = this.getParentIndex(index);
        if (parentIndex === null) {
            return
        }
        if (!this.cmp(this.heap[parentIndex], this.heap[index])) {
            // 不满足条件
            const tmp = this.heap[parentIndex];
            this.heap[parentIndex] = this.heap[index];
            this.heap[index] = tmp;
            this.siftUp(parentIndex);
        }
    }

    private heapify() { // O(N)
        // 从最后一个非叶子节点往前，逐个节点进行sift down操作
        // 最后一个非叶子节点：最后一个节点的父亲节点
        if (this.heap.length < 2) {
            return;
        }
        const lastNonLeafIndex = this.getParentIndex(this.heap.length - 1);
        for (let i = lastNonLeafIndex; i >= 0; i--) {
            // sift down
            this.siftDown(i);
        }
    }

    constructor(initList: T[], cmp: CompareFunc<T>) {
        this.heap = [...initList];
        this.cmp = cmp;
        this.heapify();
    }

    add(item: T) { // O(logN)
        this.heap.push(item);
        this.siftUp(this.heap.length - 1);
    }

    pop() { // O(logN)
        if (this.getSize() === 0) {
            throw RangeError('不能从空的堆中取出元素');
        }
        const result = this.heap[0];
        const lastOne = this.heap.pop();
        this.heap[0] = lastOne;
        this.siftDown(0);
        return result;
    }

    getSize() {
        return this.heap.length;
    }
}