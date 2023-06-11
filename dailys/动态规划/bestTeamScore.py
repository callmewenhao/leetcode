# -*- coding: utf-8 -*-

"""
@File    : bestTeamScore.py
@Author  : wenhao
@Time    : 2023/3/22 13:27
@LC      : 1626
"""
from typing import List


class Solution:
    # 最长递增子序列 的变换题目
    # 找个符合要求的最大值 然后 + 当前值
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        s = sorted(zip(scores, ages))
        f = [0] * len(s)
        for i, (score, age) in enumerate(s):
            for j in range(i):
                if s[j][1] <= age:
                    f[i] = max(f[i], f[j])
            f[i] += score
        return max(f)

    # 数据范围 1 <= scores.length, ages.length <= 1000 告诉我们这是一个 DP 题目 😁
    # 不过要先 升序排序
    # 我们从年龄最小的出发不断计算 dp 数组的值
    # 然后就是考虑 DP 细节
    # dp[i] 代表选第 i 个值是能够得到的最大分数 👍
    # 答案就是 max(dp)
    # 状态转移方程：
    # i 之前的人 j
    # 如果 j 是同龄人  f[i] = max(f[i], f[j] + s[i][0])
    # 如果 j 是小于 i 的人 且分数不冲突  f[i] = max(f[i], f[j] + s[i][0])
    # 优化 因为我们已经升序排序 也意味着 i 前面的人
    # 同龄人的分数一定小于 i 的分数 而分数大于 i 的人 一定是年轻人
    # 两者统一成 分数小于 i 的人 😁
    # 状态转移方程可以优化为
    # if s[i][0] >= s[j][0]: f[i] = max(f[i], f[j] + s[i][0])
    def bestTeamScore1(self, scores: List[int], ages: List[int]) -> int:
        s = sorted(zip(ages, scores))  # , key=lambda p: (p[1], p[0]) fuck 其实不加key就是全部升序排列 😢
        f = [0] * len(s)
        for i in range(len(s)):
            for j in range(i):
                if s[i][1] >= s[j][1]:
                    f[i] = max(f[i], f[j])
            f[i] += s[i][1]
        return max(f)
