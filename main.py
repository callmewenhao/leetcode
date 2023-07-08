# -*- coding: utf-8 -*-

"""
@File    : main.py
@Author  : wenhao
@Time    : 2023/1/30 11:38
"""
# a = [[1, 2], [2, 3], [100, -1], [2, -1], [1, 100], [100, 100]]
# print(sorted(a, key=lambda x:(x[1], x[0])))  # 先第2维升序 再第1维升序


# 区间连续子数组的和
nums = [1, 0, 3]

ans = s = 0
for i, x in enumerate(nums):
    s = s + (i+1) * x
    ans += s
print(ans)



