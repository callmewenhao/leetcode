# -*- coding: utf-8 -*-

"""
@File    : MaxQueue.py
@Author  : wenhao
@Time    : 2023/2/16 19:47
@LC      : 
"""
from collections import deque


class MaxQueue:

    def __init__(self):
        self.q = []
        self.dq = deque()

    def max_value(self) -> int:
        if not self.dq:
            return -1
        return self.dq[0]

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.dq and self.dq[-1] < value:
            self.dq.pop()
        self.dq.append(value)

    def pop_front(self) -> int:
        if not self.q:
            return -1
        val = self.q.pop(0)
        if val == self.dq[0]:
            self.dq.popleft()
        return val

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
