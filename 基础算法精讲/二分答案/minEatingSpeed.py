# -*- coding: utf-8 -*-

"""
@File    : minEatingSpeed.py
@Author  : wenhao
@Time    : 2023/2/9 20:23
@LC      : 875
"""
from typing import List


class Solution:
    '''
    最小化最大值->经典二分查找答案
    首先，吃香蕉的速度范围是：1~max(piles)，max(piles) + n 的效果和他本身一样，答案s就在其中
    答案速度~max(piles)，即[s, max(pils)],都可以在h时间内把🍌吃完
    而[1, max(pils) - 1]，都吃不完，这就体现了二分性👏
    我们使用经典的二分闭区间写法寻找即可
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        def check(s: int) -> bool:
            t = 0
            for num in piles:
                t += (num + s - 1) // s  # 向上整除，计算吃🍌的时间
                if t > h:
                    return False
            return True

        l, r = 1, max(piles)
        while l <= r:
            m = l + (r - l) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l
