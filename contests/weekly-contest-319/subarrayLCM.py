from typing import List
from math import lcm


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            LCM = 1
            for j in range(i, n):
                LCM = lcm(LCM, nums[j])
                if LCM > k: break;
                if LCM == k: ans += 1
        return ans