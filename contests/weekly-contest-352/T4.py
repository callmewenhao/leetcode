# -*- coding: utf-8 -*-

"""
@File    : T4.py
@Author  : wenhao
@Time    : 2023/7/3 9:45
@LC      : 
"""
from typing import List

# 思路 1 数据范围 1000 尝试暴力枚举连续子数组 使用 vis 数组表示当前枚举过程中已经遇到过的数字
# 思路 2 贡献法 枚举每个值对不平衡数值的贡献 即包含该值的区间数目 = 左端点个数 * 右端点个数  注意还要减去不合法的贡献

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        right = [0] * n  # nums[i] 右侧的 x 和 x-1 的最近下标（不存在时为 n）
        idx = [n] * (n + 1)
        for i in range(n - 1, -1, -1):
            x = nums[i]
            right[i] = min(idx[x], idx[x - 1])
            idx[x] = i

        ans = 0
        idx = [-1] * (n + 1)
        for i, (x, r) in enumerate(zip(nums, right)):
            # 统计 x 能产生多少贡献
            ans += (i - idx[x - 1]) * (r - i)  # 子数组左端点个数 * 子数组右端点个数
            idx[x] = i
        # 上面计算的时候，每个子数组的最小值必然可以作为贡献，而这是不合法的
        # 所以每个子数组都多算了 1 个不合法的贡献
        return ans - n * (n + 1) // 2


    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i, x in enumerate(nums):
            vis = [False] * (n + 2)
            vis[x] = True
            cnt = 0
            for j in range(i+1, n):
                y = nums[j]
                if not vis[y]:
                    cnt += 1 - vis[y-1] - vis[y+1]
                    vis[y] = True
                ans += cnt

        return ans


