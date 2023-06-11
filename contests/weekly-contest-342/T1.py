# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/4/23 9:59
@LC      : 
"""
from typing import List
from collections import Counter
from functools import cache
from itertools import pairwise, accumulate

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24






