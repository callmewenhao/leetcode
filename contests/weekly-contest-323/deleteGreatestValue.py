from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
           row.sort()
        # ans = 0
        # for col in zip(grid):
        #     ans += max(col)
        # return ans

        return sum(max(col) for col in zip(*grid))
