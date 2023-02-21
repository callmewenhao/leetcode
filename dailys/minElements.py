from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        dis = abs(s - goal)
        return dis // limit + (dis % limit != 0)

