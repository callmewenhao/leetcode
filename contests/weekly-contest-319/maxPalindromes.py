class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(2 * n - 1):
            l = i // 2
            r = l + i % 2
            dp[l + 1] = max(dp[l], dp[l + 1])
            while 0 <= l and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    dp[r + 1] = max(dp[l] + 1, dp[r + 1])
                l -= 1
                r += 1

        return dp[n]
