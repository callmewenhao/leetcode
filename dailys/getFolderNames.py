# -*- coding: utf-8 -*-

"""
@File    : getFolderNames.py
@Author  : wenhao
@Time    : 2023/3/3 9:03
@LC      : 1487
"""
from typing import List
from collections import defaultdict

class Solution:
    # 总体不难 但是细节很多 😒
    # 思路分析
    # 用字典存 所有出现过的名字
    # 如果命名一个没出现过的名字 那就直接命名并 将 hash 值设置为新编号
    # 如果命名一个出现过的名字 根据编号找一个新名字 判断这个新名字是否冲突
    # 不冲突就命名 同时加到字典里 否则就一直找新名字
    def getFolderNames(self, names: List[str]) -> List[str]:
        n = len(names)
        m = defaultdict()

        ans = [""] * n
        for i, name in enumerate(names):
            if name not in m:
                ans[i] = name
                m[name] = 1
            else:
                new_name = name + '(' + str(m[name]) + ')'
                m[name] += 1
                while new_name in m:
                    new_name = name + '(' + str(m[name]) + ')'
                    m[name] += 1
                m[new_name] = 1
                ans[i] = new_name
        return ans








