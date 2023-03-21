# -*- coding: utf-8 -*-

"""
@File    : atMostNGivenDigitSet.py
@Author  : wenhao
@Time    : 2023/3/20 16:52
@LC      : 902
"""
from typing import List
from functools import cache


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, limit: bool, lead: bool) -> int:
            if i == len(s):  # 所有位置都访问完之后
                return int(lead)  # 注意不包含 0 因为数据范围就不含 0
            res = 0
            # 前面没数时可以选择不选 或者从 1 开始选
            if not lead:  # 选择跳过
                res = f(i + 1, False, False)
            # 选数
            up = s[i] if limit else '9'  # 确定上界
            # 枚举要填的数字
            for d in digits:  # 答案更新
                if d > up:
                    break
                res += f(i + 1, limit and d == up, True)
            return res

        # 从第 0 位开始，mask 初始值 0 有限制 没数
        return f(0, True, False)
