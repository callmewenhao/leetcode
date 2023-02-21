import collections
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        s = set()
        nums.sort()

        for i in range(len(nums) // 2):
            x = nums[i]
            y = nums[-1 - i]
            s.add(x + y)

        return len(s)

    def distinctAverages_one_line(self, nums: List[int]) -> int:
        nums.sort()
        return len(set(nums[i] + nums[-i - 1] for i in range(len(nums) // 2)))
