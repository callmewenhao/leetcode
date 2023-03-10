# -*- coding: utf-8 -*-

"""
@File    : minimumRecolors.py
@Author  : wenhao
@Time    : 2023/3/9 9:20
@LC      : minimumRecolors
"""


class Solution:
    # 滑窗优化
    def minimumRecolors1(self, blocks: str, k: int) -> int:
        ans = cnt_w = blocks[:k].count('W')
        for in_, out_ in zip(blocks[k:], blocks):  # 灵神 👍
            cnt_w += (in_ == 'W') - (out_ == 'W')
            ans = min(ans, cnt_w)
        return ans

    # 暴力枚举
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = n
        for i in range(n - k):
            cnt = 0
            for j in range(k):
                if blocks[i + j] == 'W':
                    cnt += 1
            ans = min(ans, cnt)
        return ans
