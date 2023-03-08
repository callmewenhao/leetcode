# -*- coding: utf-8 -*-

"""
@File    : minimumDeletions.py
@Author  : wenhao
@Time    : 2023/3/6 8:45
@LC      : 1653
"""


class Solution:
    # dp
    # https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/solutions/2149746/qian-hou-zhui-fen-jie-yi-zhang-tu-miao-d-dor2/
    def minimumDeletions1(self, s: str) -> int:
        f = cnt_b = 0
        for i, c in enumerate(s):
            if c == 'b':
                cnt_b += 1
            else:
                f = min(f + 1, cnt_b)
        return f


    # 2 次遍历 统计前后缀中的 b 和 a 的个数
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        # 统计前缀 b 的个数
        b = [0] * (n + 1)
        for i, c in enumerate(s):
            b[i + 1] = b[i] + (1 if c == 'b' else 0)

        # 统计后缀 a 的个数
        a = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            a[i] = a[i + 1] + (1 if s[i] == 'a' else 0)

        # 统计答案
        ans = n
        for i in range(n + 1):  # 😣
            ans = min(ans, a[i] + b[i])
        return ans

