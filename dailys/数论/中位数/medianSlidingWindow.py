# -*- coding: utf-8 -*-

"""
@File    : medianSlidingWindow.py
@Author  : wenhao
@Time    : 2023/3/21 22:12
@LC      : 480
"""
from typing import List
import heapq
from collections import Counter


class MedianFinder:
    def __init__(self, k: int):
        """
        initialize your data structure here.
        """
        self.min_heap = []  # 小根堆
        heapq.heapify(self.min_heap)
        self.max_heap = []  # 大根堆
        heapq.heapify(self.max_heap)
        # 延迟删除
        self.cnt = Counter()
        # 统计 左元素个数 - 右元素个数
        self.balance = 0
        # 记录一下 k
        self.k = k

    def addNum(self, num: int) -> None:
        # 不能用个数判断
        if self.balance == 0:
            heapq.heappush(self.min_heap, num)
            mi = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -mi)
            self.balance += 1  # 左边元素+1
            return
        # n+1,n -> n+1,n+1
        heapq.heappush(self.max_heap, -num)
        mx = -1 * heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, mx)
        self.balance -= 1  # 右边元素+1
        # 维护一下堆
        self.maintainHeap()

    # 延迟删除函数
    def deleteNum(self, num):
        self.cnt[num] += 1
        # 删除元素的大小 影响 self.balance
        if self.min_heap and num >= self.min_heap[0]:
            self.balance += 1  # 右边元素-1
        else:
            self.balance -= 1  # 左边元素-1
        # 处理 self.balance 不平衡的情况 移动元素
        # self.balance 一共四种情况
        # 0 -> 1 or -1
        # 1 -> 2 or 0
        # 0       不用处理
        # 1       不用处理
        # 2       大根堆 -> 小根堆 一个元素
        # -1      小根堆 -> 大根堆 一个元素
        if self.balance == 2:
            mx = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, mx)
            self.balance = 0
        if self.balance == -1:
            mi = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -mi)
            self.balance = 1
        # 维护一下堆  不能删 🤣
        self.maintainHeap()

    def findMedian(self) -> float:
        if self.k & 1 == 0:
            return (-1 * self.max_heap[0] + self.min_heap[0]) / 2
        return -1 * self.max_heap[0]

    def maintainHeap(self):
        # 如果当前队列头就是待删除元素 立即删除 保证求取平均值时的堆顶元素可取 🤗
        while self.min_heap and self.cnt[self.min_heap[0]] > 0:
            self.cnt[self.min_heap[0]] -= 1
            heapq.heappop(self.min_heap)
        while self.max_heap and self.cnt[-1 * self.max_heap[0]] > 0:
            self.cnt[-1 * self.max_heap[0]] -= 1
            heapq.heappop(self.max_heap)


class Solution:
    # 双优先队列 + 延迟删除
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 初始化 先把前 k-1 个元素放进去
        mf = MedianFinder(k)
        for i in range(k - 1):
            mf.addNum(nums[i])
        ans = []
        # 然后 一放一求一删除
        for i in range(k - 1, len(nums)):
            mf.addNum(nums[i])
            # print("add", nums[i], mf.max_heap, mf.min_heap)
            ans.append(mf.findMedian())
            mf.deleteNum(nums[i - k + 1])
            # print("delete", nums[i - k + 1], mf.max_heap, mf.min_heap)
        return ans
