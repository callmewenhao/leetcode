from typing import List



class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < target:
                ans += j - i
                i += 1
            else:
                j -= 1
        return ans % 1000000007