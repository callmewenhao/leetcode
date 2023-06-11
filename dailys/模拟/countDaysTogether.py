# -*- coding: utf-8 -*-

"""
@File    : countDaysTogether.py
@Author  : wenhao
@Time    : 2023/4/17 9:07
@LC      : 2409
"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        arriveTime = max(arriveAlice, arriveBob)
        leaveTime = min(leaveAlice, leaveBob)

        a_m, a_d = int(arriveTime[0:2]), int(arriveTime[3:])
        l_m, l_d = int(leaveTime[0:2]), int(leaveTime[3:])

        if a_m > l_m: return 0
        if a_m == l_m:
            if a_d > l_d: return 0
            return l_d - a_d + 1
        ans = (m[a_m] - a_d + 1) + l_d
        for i in range(a_m + 1, l_m):
            ans += m[i]
        return ans















