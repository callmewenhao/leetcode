# -*- coding: utf-8 -*-
from typing import List


# 多重背包
# 基础版本 背包能够装的最大值

weights = [1, 3, 4, 5]
values = [15, 20, 30, 40]
nums = [2, 3, 2, 3]
bagWeight = 12

# 一维数组版本
def multiBag(weights: List[int], values: List[int], nums: List[int], bagWeight: int) -> int:
    dp = [0] * (bagWeight + 1)  # 初始化全 0
    for i, (weight, value) in enumerate(zip(weights, values)):  # 物品 i 重量为 weight
        for j in range(bagWeight, weight - 1, -1):  # 背包容量 j
            # 枚举同一物品的选取个数 k
            cnt = min(nums[i], j // weight)
            for k in range(1, cnt + 1):
                dp[j] = max(dp[j], dp[j - k * weight] + k * value)
        print(dp)
    return dp[bagWeight]

# 二进制优化版本
def multiBagBi(weights: List[int], values: List[int], nums: List[int], bagWeight: int) -> int:
    
    # 重新计算物品 重量 价值
    new_weights = []
    new_values = []

    # 借助二进制优化物品 重量和价值
    
    for weight, value, num in zip(weights, values, nums):
        c = 1  # 1, 2, 4, 8, ...
        while num > c:
            num -= c
            new_weights.append(c * weight)
            new_values.append(c * value)
            c *= 2
        new_weights.append(num * weight)
        new_values.append(num * value)
    
    # 套一个 01 背包模板 👏
    dp = [0] * (bagWeight + 1)  # 初始化全 0
    for weight, value in zip(new_weights, new_values):
        for j in range(bagWeight, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)
        print(dp)
            
    return dp[bagWeight]

    
ans = multiBagBi(weights, values, nums, bagWeight)

print(ans)





                
                    









