# -*- coding: utf-8 -*-

"""
@File    : numDupDigitsAtMostN.py
@Author  : wenhao
@Time    : 2023/3/20 11:02
@LC      : 1012
"""
from typing import List
from functools import cache

class Solution:
    # 正难则反
    # 答案就是返回 n - 不重复的数字个数
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)

        # 从 i 开始填数字
        # i 前面填的数字的集合是 mask
        # 返回 能构造出的特殊整数的数目
        # limit 表示前面填的数字是否都是 n 对应位上的
        # 如果 limit=true 那么当前位至多为 s[i] 否则至多为 9
        # lead 表示前面是否填了数字（是否跳过）
        # 如果 lead=true 当前位可以从 0 开始 否则从 1 开始 或者继续跳过
        @cache
        def f(i: int, mask: int, limit: bool, lead: bool) -> int:
            if i == len(s):  # 所有位置都访问完之后
                return int(lead)  # 注意不包含 0 因为数据范围就不含 0
            res = 0
            # 前面没数时可以选择不选 或者从 1 开始选
            if not lead:  # 选择跳过
                res = f(i + 1, mask, False, False)
            # 选数
            low = 1 - int(lead)  # 确定下界
            up = int(s[i]) if limit else 9  # 确定上界
            # 枚举要填的数字
            for d in range(low, up + 1):  # 答案更新
                if ((mask >> d) & 1) == 0:  # mask 中没有 d 才能更新
                    res += f(i + 1, mask | (1 << d), limit and d == up, True)
            return res
        return n - f(0, 0, True, False)