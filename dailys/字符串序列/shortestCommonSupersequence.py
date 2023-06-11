# -*- coding: utf-8 -*-

"""
@File    : shortestCommonSupersequence.py
@Author  : wenhao
@Time    : 2023/3/28 21:42
@LC      : 1092
"""
from functools import cache


class Solution:
    # 记忆化搜索·进一步优化 😜
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        # dfs(i,j) 返回 s 的前 i 个字母和 t 的前 j 个字母的最短公共超序列的长度
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0: return j + 1
            if j < 0: return i + 1
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + 1
            return min(dfs(i - 1, j), dfs(i, j - 1)) + 1

        # make_ans(i,j) 返回 s 的前 i 个字母和 t 的前 j 个字母的最短公共超序列
        # 看上去和 dfs 没啥区别，但是末尾的递归是 if-else
        # make_ans(i-1,j) 和 make_ans(i,j-1) 不会都调用
        # 所以 make_ans 的递归树仅仅是一条链
        def make_ans(i: int, j: int) -> str:
            if i < 0: return t[:j + 1]
            if j < 0: return s[:i + 1]
            if s[i] == t[j]:
                return make_ans(i - 1, j - 1) + s[i]
            # 如果下面 if 成立，说明上面 dfs 中的 min 取的是 dfs(i - 1, j)
            # 说明 dfs(i - 1, j) 对应的公共超序列更短
            # 那么就在 make_ans(i - 1, j) 的结果后面加上 s[i]
            # 否则说明 dfs(i, j - 1) 对应的公共超序列更短
            # 那么就在 make_ans(i, j - 1) 的结果后面加上 t[j]
            if dfs(i, j) == dfs(i - 1, j) + 1:
                return make_ans(i - 1, j) + s[i]
            return make_ans(i, j - 1) + t[j]

        return make_ans(len(s) - 1, len(t) - 1)

    # 记忆化搜索 初步优化 😂
    # 能通过的测试数据更多，但仍然超时（超内存），还需要进一步优化
    def shortestCommonSupersequence2(self, s: str, t: str) -> str:
        # dfs(i,j) 返回 s 的前 i 个字母和 t 的前 j 个字母的最短公共超序列
        @cache
        def dfs(i: int, j: int) -> str:
            if i < 0: return t[:j + 1]
            if j < 0: return s[:i + 1]
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + s[i]
            ans1 = dfs(i - 1, j)
            ans2 = dfs(i, j - 1)
            if len(ans1) < len(ans2):
                return ans1 + s[i]
            return ans2 + t[j]

        return dfs(len(s) - 1, len(t) - 1)

    # 会超时的递归代码 😁
    def shortestCommonSupersequence1(self, s: str, t: str) -> str:
        if s == "":
            return t  # s 是空串，返回剩余的 t
        if t == "":
            return s  # t 是空串，返回剩余的 s
        if s[-1] == t[-1]:  # 最短公共超序列一定包含这个相同的字符
            return self.shortestCommonSupersequence(s[:-1], t[:-1]) + s[-1]
        ans1 = self.shortestCommonSupersequence(s[:-1], t)
        ans2 = self.shortestCommonSupersequence(s, t[:-1])
        if len(ans1) < len(ans2):
            return ans1 + s[-1]
        return ans2 + t[-1]
