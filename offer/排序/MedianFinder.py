# -*- coding: utf-8 -*-

"""
@File    : MedianFinder.py
@Author  : wenhao
@Time    : 2023/2/3 12:59
@LC      : 
"""
from bisect import insort_left


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
