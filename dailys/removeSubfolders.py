# -*- coding: utf-8 -*-

"""
@File    : removeSubfolders.py
@Author  : wenhao
@Time    : 2023/2/8 19:30
@LC      : 1233
"""
from typing import List


class Solution:
    # optimize
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]

        for i in range(1, len(folder)):
            if not ((pre := len(ans[-1])) < len(folder[i]) and ans[-1] == folder[i][:pre] and folder[i][pre] == '/'):
                ans.append(folder[i])
        return ans



    # 排序 + set + 枚举前缀
    def removeSubfolders1(self, folder: List[str]) -> List[str]:
        folder.sort()
        s= set()

        ans = []
        for path in folder:
            res = path.split('/')
            p = ''
            flag = True
            for x in res:
                p += x
                if p in s:
                    flag = False
            s.add(p)
            if flag:
                ans.append(path)
        return ans







