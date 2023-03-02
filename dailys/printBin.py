# -*- coding: utf-8 -*-

"""
@File    : printBin.py
@Author  : wenhao
@Time    : 2023/3/2 8:59
@LC      : 
"""


class Solution:
    # 灵神的思路 位数不超 6 下述过程最多 6 步
    # 其实计算过程 在危机原理中学过
    # 把小数不断 *2
    # 结果小于 1 就进位 0
    # 结果大于 1 就进位 1 然后 结果减 1
    # 重复上述操作
    def printBin(self, num: float) -> str:
        s = ["0."]
        for _ in range(6):
            num *= 2
            if num < 1:
                s.append('0')
            else:
                s.append('1')
                num -= 1
                if num == 0:
                    return ''.join(s)
        return "ERROR"

    # 我的思路 打表 + 二分 + 递归
    def printBin(self, num: float) -> str:
        # 打表
        bins = [1] * 31
        for i in range(1, 31):
            bins[i] = bins[i - 1] * 0.5

        # 递归
        def dfs(num: float, ans: str) -> str:
            if num == 0:
                return ans
            # 二分查找
            l, r = 1, 30
            while l <= r:
                mid = l + (r - l) // 2
                if bins[mid] > num:
                    l = mid + 1
                else:
                    r = mid - 1

            if l > 30:
                return "ERROR"
            # 计算要加多少个 0
            nums_0 = l - (len(ans) - 2) - 1
            ans += "".join(['0' for _ in range(nums_0)])
            # 加一个 1
            ans += '1'
            # 递归 处理剩余值
            return dfs(num - bins[l], ans)

        return dfs(num, "0.")
