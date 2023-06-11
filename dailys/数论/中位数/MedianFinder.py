# -*- coding: utf-8 -*-

"""
@File    : MedianFinder.py
@Author  : wenhao
@Time    : 2023/3/21 21:51
@LC      : 295
"""
import heapq


class MedianFinder:
    # 双优先队列 小根堆 + 大根堆
    # 中位数求法
    # 如果 奇数个元素 大根堆n+1个元素  小根堆n个元素 返回 大根堆根
    # 如果 偶数个元素 大根堆n个元素  小根堆n个元素 返回 大根堆根和小根堆根的均值
    # 维护两个队列 插入
    # 当 大根堆n个元素  小根堆n个元素 时  放入小根堆 再把小根堆根 放入大根堆  n,n -> n+1,n
    # 当 大根堆n+1个元素  小根堆n个元素 时  放入大根堆 再把大根堆根 放入小根堆 n+ 1,n+1-> n+1,n+1
    # 注意 py 默认 小根堆 🤣
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []  # 小根堆
        heapq.heapify(self.min_heap)
        self.max_heap = []  # 大根堆
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, num)
            mi = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -mi)
            return
        heapq.heappush(self.max_heap, -num)
        mx = -1 * heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, mx)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-1 * self.max_heap[0] + self.min_heap[0]) / 2
        return -1 * self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
