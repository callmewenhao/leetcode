# -*- coding: utf-8 -*-

"""
@File    : T4.py
@Author  : wenhao
@Time    : 2023/5/17 22:16
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter

"""
问题分析

下标与结果无关 因此对数组进行排序 从大到小

枚举每个最大值 nums[i] 考虑所有的最小值

如：a, b, c, d, e  由小到大

当枚举到 d 时

min = a*2^2 + b*2^1 + c*2^0  
解释 a 为最小值时的区间个数取决于 b, c 选还是不选 故有 2^2 种
同理得到 b c 为最小值时的区间个数
令 s = a*2^2 + b*2^1 + c*2^0  故此时力量为 ans += (d + s) * d^2

枚举到 e 时

min = a*2^3 + b*2^2 + c*2^1 + d*2^0 = 2 * (a*2^2 + b*2^1 + c*2^0) + d
这就是新的 s' = 2 * (a*2^2 + b*2^1 + c*2^0) + d = 2 * s + d
故此时力量为 ans += (e + s') * e^2

然后继续更新 s'' 计算新的答案
"""


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = s = 0
        for x in nums:
            ans = (ans + (x + s) * x * x) % MOD
            s = (s * 2 + x) % MOD
        return ans
