# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/6/18 10:31
@LC      : 
"""

from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        ans = 0
        while mainTank:
            if mainTank >= 5:
                ans += 5 * 10
                mainTank -= 5
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                ans += mainTank * 10
                mainTank = 0

        return ans