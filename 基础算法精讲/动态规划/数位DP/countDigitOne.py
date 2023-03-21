# -*- coding: utf-8 -*-

"""
@File    : countDigitOne.py
@Author  : wenhao
@Time    : 2023/3/20 20:15
@LC      : 233
"""
from functools import cache


class Solution:
    # 就是那道 digit 题目改的 https://zhuanlan.zhihu.com/p/348851463
    # 改自灵神的数位 DP 模板
    # 因为是求 1 的个数，所以不用考虑前导 0 的影响 如果是求 0 的个数就要考虑了
    def countDigitOne(self, n: int) -> int:
        s = str(n)  # 转字符串

        @cache
        def f(i: int, cnt: int, limit: int) -> int:
            if i == len(s):  # 数位遍历完成 返回数字个数
                return cnt
            res = 0
            up = int(s[i]) if limit else 9  # 确定上界
            for d in range(up + 1):
                if d == 1:  # 如果当前位选 1
                    res += f(i + 1, cnt + 1, limit and d == up)
                else:  # 不选 1
                    res += f(i + 1, cnt, limit and d == up)
            return res

        return f(0, 0, True)
