# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/2/18 22:19
@LC      : 2566
"""
class Solution:
    # 灵神 时间复杂度 log num
    def minMaxDifference(self, num: int) -> int:
        mx = mi = num
        s = str(num)
        for c in s:
            if c != '9':  # 替换第一个不为 9 的数
                mx = int(s.replace(c, '9'))
                break
        for c in s:
            if c != '0':  # 替换第一个不为 0 的数
                mi = int(s.replace(c, '0'))
                break
        return mx - mi


    # 比赛时的写法
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        mx = ""
        c = ''
        for i in range(len(s)):
            if s[i] == '9':
                mx += '9'
            elif s[i] != '9':
                if c == '':
                    mx += '9'
                    c = s[i]
                elif c == s[i]:
                    mx += '9'
                else:
                    mx += s[i]

        mi = ""
        c = ''
        for i in range(len(s)):
            if s[i] == '0':
                mi += '0'
            elif s[i] != '0':
                if c == '':
                    mi += '0'
                    c = s[i]
                elif c == s[i]:
                    mi += '0'
                else:
                    mi += s[i]

        return int(mx) - int(mi)














