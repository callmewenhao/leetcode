# -*- coding: utf-8 -*-

"""
@File    : grayCode.py
@Author  : wenhao
@Time    : 2023/2/23 15:46
@LC      : 89
"""
from typing import List


class Solution:
    # 方法 2 数学公式
    # 第 i个 gray码为 i^(i // 2)
    def grayCode2(self, n: int) -> List[int]:
        ans = [0] * (1 << n)  # 一共 2^n 个数
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i  # 挨个构造
        return ans

    # 方法 1 归纳总结
    def grayCode1(self, n: int) -> List[int]:
        ans = [0]  # 答案 个数是 2^n
        for i in range(1, n + 1):  # 模拟 2 的 i 次方
            for j in range(len(ans) - 1, -1, -1):  # 倒序遍历
                ans.append(ans[j] | (1 << (i - 1)))  # 构造新数
        return ans
