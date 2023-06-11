# -*- coding: utf-8 -*-

"""
@File    : 1416numberOfArrays.py
@Author  : wenhao
@Time    : 2023/4/23 9:29
@LC      : 1416
"""
from functools import cache


class Solution:
    # 分隔数组以得到最大和 的变形题目
    # 记搜
    def numberOfArrays(self, s: str, k: int) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 1  # 成功找到一种方案
            res = 0
            for j in range(i, -1, -1):
                num = s[j:i + 1]
                # 前导 0 不合法
                if num[0] == '0':
                    continue
                # 防止出现特大数
                if len(num) > len(str(k)):
                    break
                # 数字值
                num = int(num)
                # 大于范围也不合法
                if num > k:
                    break
                # 更新答案
                res += dfs(j - 1)
            return res % (10 ** 9 + 7)

        return dfs(len(s) - 1)

    # 递推
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        m = len(str(k))  # k 的数位
        f = [1] + [0] * n

        for i in range(n):
            # 枚举数位个数
            for j in range(i, -1, -1):
                # 范围限制
                if i - j + 1 > m:
                    break
                num = s[j: i + 1]
                if num[0] == '0':
                    continue
                num = int(num)
                if num > k:
                    break
                f[i + 1] += f[j]
                f[i + 1] %= (10 ** 9 + 7)

        return f[-1]
