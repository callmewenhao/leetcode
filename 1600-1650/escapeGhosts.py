# -*- coding: utf-8 -*-

"""
@File    : escapeGhosts.py
@Author  : wenhao
@Time    : 2023/2/1 21:08
@LC      : 789
"""
from typing import List

class Solution:
    # 我愿称之为脑筋急转弯
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # 计算 曼哈顿距离 就行
        d1 = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            d2 = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if d1 >= d2:
                return False
        return True
