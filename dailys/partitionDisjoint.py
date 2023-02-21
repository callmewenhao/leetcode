from typing import List
from math import inf

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ans = 0
        left_max = [nums[0]] * len(nums)
        right_min = [inf] * len(nums)
        for i in range(1, len(nums)):
            left_max[i] = max(nums[i], left_max[i - 1])

        ans = 0
        for i in range(len(nums) - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i + 1])
            if right_min[i] >= left_max[i]:
                ans = i + 1
        return  ans