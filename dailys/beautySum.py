from collections import Counter
from collections import defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            cnt = defaultdict(int)
            for j in range(i, len(s)):
                cnt[s[j]] += 1
                ans += max(cnt.values()) - min(cnt.values())
        return ans
