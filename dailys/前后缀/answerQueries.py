# -*- coding: utf-8 -*-

"""
@File    : answerQueries.py
@Author  : wenhao
@Time    : 2023/3/17 9:20
@LC      : 2389
"""
from typing import List
from itertools import accumulate
from bisect import bisect_right


class Solution:
    # 贪心 + 前缀和
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre = list(accumulate(nums))

        # ans = [0] * len(queries)
        # for i, q in enumerate(queries):
        #     ans[i] = bisect_right(pre, q)
        #
        # return ans

        return [bisect_right(pre, q) for q in queries]





