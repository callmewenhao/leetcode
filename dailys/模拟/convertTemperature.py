# -*- coding: utf-8 -*-

"""
@File    : convertTemperature.py
@Author  : wenhao
@Time    : 2023/3/21 10:04
@LC      : 2469
"""
from typing import List


class Solution:
    # py 骚操作 🤣
    def convertTemperature(self, celsius: float) -> List[float]:
        开氏度 = celsius + 273.15
        华氏度 = celsius * 1.80 + 32.00
        return [开氏度, 华氏度]

