class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n

        for start in range(n):
            if s[start] == "0":
                continue
            for end in range(start + 1, n + 1):
                if 0 < int(s[start:end]) < 27:
                    dp[end] += dp[start]

        return dp[n]
