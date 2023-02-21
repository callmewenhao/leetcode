# -*- coding: utf-8 -*-

"""
@File    : singleNumbers.py
@Author  : wenhao
@Time    : 2023/2/8 19:07
@LC      : 
"""
from typing import List


class Solution:
    '''
    思路：为了区分这两个数，我们需要找到他们的某个不同的二进制位：这就可以使用异或的结果
    用 m 保存从右向左的第一个不同的二进制位，然后使用这一位对 nums 划分，
    划分的两个组内元素的异或结果就是答案
    '''
    def singleNumbers(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        m = 1
        while m & xor == 0:
            m <<= 1

        x, y = 0, 0
        for num in nums:
            if m & num:
                x ^= num
            else:
                y ^= num

        return [x, y]

