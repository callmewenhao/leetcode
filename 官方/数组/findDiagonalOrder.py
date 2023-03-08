# -*- coding: utf-8 -*-

"""
@File    : findDiagonalOrder.py
@Author  : wenhao
@Time    : 2023/3/4 14:28
@LC      : 498
"""
from typing import List


class Solution:
    # S 遍历
    # 把对角线编号 分成奇偶两种情况遍历
    # 然后 根据编号 来确定起点
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        ans = []
        for i in range(m + n - 1):  # 对角线
            if (i & 1) == 0:  # 偶数对角线向右上遍历
                # 确定起点
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while 0 <= x and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
            else:  # 奇数对角线向左下遍历
                # 确定起点
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while x < m and 0 <= y:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
        return ans
