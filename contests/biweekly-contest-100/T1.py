# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/3/18 22:12
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    # 优化
    # 其实就是分类讨论的思想 😁
    def distMoney(self, money: int, children: int) -> int:
        # 先每人分配 1 元
        money -= children
        if money < 0:  # 不够分？返回-1
            return -1
        ans = min(money // 7, children)  # 初步分配 每人分 8 元
        money -= ans * 7  # 剩下的钱数
        children -= ans  # 有多少
        # if children == 0 and money 必须找一个前面分了 8 元的人 分配剩余的钱
        # if children == 1 and money == 3 剩余一个孩子且刚好剩余3 元 不能有人分配到 4 元
        if children == 0 and money or \
                children == 1 and money == 3:
            ans -= 1
        return ans

    def distMoney1(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        n = money // 7
        mod = money % 7
        if n > children:
            return n - 1
        if n == children:
            if mod == 0:
                return n
            else:
                return n - 1
        if n + 1 == children:
            if mod == 3:
                return max(0, n - 1)
            else:
                return n
        return n
