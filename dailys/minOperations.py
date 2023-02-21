from typing import List



class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i, val in enumerate(nums):
            if i == 0: continue
            if nums[i - 1] + 1 > val:
                ans += nums[i - 1] + 1 - val
                nums[i] = nums[i - 1] + 1
        return ans
