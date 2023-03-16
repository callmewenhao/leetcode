# -*- coding: utf-8 -*-

"""
@File    : beautifulSubarrays.py
@Author  : wenhao
@Time    : 2023/3/5 20:31
@LC      : 2585
"""
from typing import List


# 互质：左半部分 和 右半部分 没有公共质因子（最大公约数是1）
# 哪些地方可以分割？
# 逆向思维：哪些地方不能分割

# 对于每个质因，都处理它在 nums 中的最左边的下标 和 最右边的下标 left right
# 那么答案不能在 [left, right) => 最小的答案可能是 right

# 答案是第一组区间的右端点最大值
#
# 考虑到数据范围 不必对区间进行排序
# 可以考虑使用 right[i] 记录 i 是左端点的情况 对应右端点最大值

# 1. 分解质因子
# 2. 区间处理

class Solution:

    def findValidSplit(self, nums: List[int]) -> int:
        left = {}  # left[p] = p首次出现的下标
        right = [-1] * len(nums)  # right[i] 记录下标i是左端点时的右端点最大值

        # p 是质因子 i 是对应的下标
        def f(p: int, i: int) -> None:
            if p in left:
                right[left[p]] = i
            else:
                left[p] = i

        # 从左到右 遍历数组 找质因子 更新 left right
        for i, x in enumerate(nums):
            d = 2
            while d * d <= x:
                if x % d == 0:
                    f(d, i)
                    x //= d
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:  # 最后剩一个单独的质因子
                f(x, i)
        # 处理区间
        mx = 0
        for l, r in enumerate(right):
            if l > mx:
                return mx
            mx = max(mx ,r)
        return -1