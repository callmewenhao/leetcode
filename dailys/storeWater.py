from typing import List
from math import inf


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        ans = 0
        max_vat = max(vat)
        if max_vat == 0: return ans

        for i in range(1, max_vat + 1):






