# -*- coding: utf-8 -*-

"""
@File    : baseNeg2.py
@Author  : wenhao
@Time    : 2023/4/6 9:13
@LC      : 1017
"""


"""
除法的取整 
Python 的整除是向下取整（无论除数正负）
C++、Java 的整除是向 0 取整  除数大于 0 向下取整 除数小于 0 向上取整 
"""

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = []
        for i in range(32):
            if n >> i == 0:
                break
            if i & 1 and (n >> i) & 1:  # 奇数位置且有 1 存在
                n += (1 << (i + 1))
            ans.append(str((n >> i) & 1))

        return ''.join(ans[::-1])

        # return f"{n:b}"  # 这里应该可以优化
        # return bin(n).replace("0b","")
