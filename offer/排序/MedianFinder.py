# -*- coding: utf-8 -*-

"""
@File    : MedianFinder.py
@Author  : wenhao
@Time    : 2023/2/3 12:59
@LC      : 
"""
from bisect import insort_left
import heapq


# 优化 使用大小堆 优化时间复杂度为 log n
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []  # 小根堆 存放较大元素
        heapq.heapify(self.minHeap)  # 堆化
        self.maxHeap = []  # 大根堆 存放较大元素
        heapq.heapify(self.maxHeap)  # 堆化

    def addNum(self, num: int) -> None:
        # 两个堆长度相同时
        # 应该把一个元素 放到 minHeap 中
        # 这个元素应是 maxHeap + num 中的最大值
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush(self.maxHeap, -num)
            mx = -1. * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, mx)
        else:
            # 长度不同时
            # 应该把一个元素 放到 maxHeap 中
            # 这个元素应是 minHeap + num 中的最小值
            heapq.heappush(self.minHeap, num)
            mn = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -mn)

    def findMedian(self) -> float:
        # 返回中位数
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        return self.minHeap[0]


# 自己的做法
# 添加元素是：二分查找插入位置 + 移动元素
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.buf = []

    def addNum(self, num: int) -> None:
        if len(self.buf) == 0:
            self.buf.append(num)
            return
        # 二分查找加入的位置
        insort_left(self.buf, num)

    def findMedian(self) -> float:
        l = len(self.buf)
        return self.buf[(l - 1) // 2] if l % 2 == 1 else (self.buf[l // 2] + self.buf[l // 2 - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
