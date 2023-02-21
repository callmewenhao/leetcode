from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        ans = -1
        for num in s:
            cnt = 0
            while num in s:
                num *= num
                cnt += 1
            if cnt >= 2:
                ans = max(ans, cnt)
        return ans



