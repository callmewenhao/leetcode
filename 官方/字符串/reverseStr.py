# -*- coding: utf-8 -*-

"""
@File    : reverseStr.py
@Author  : wenhao
@Time    : 2023/3/7 10:19
@LC      : 541
"""


class Solution:
    # 稍微有一点复杂 好在 py 的切牌你很方便 😁
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s) // (2 * k)
        # 处理 2k
        for i in range(n):
            l = i * 2 * k
            r = i * 2 * k + k
            s[l:r] = s[l:r][::-1]  # 反转区间
        # 处理剩余元素
        if (m := len(s) % (2 * k)) != 0:
            l = n * 2 * k
            if m < k:
                s[l:] = s[l:][::-1]
            else:
                s[l:l + k] = s[l:l + k][::-1]
        return "".join(s)
