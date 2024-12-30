class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1e9 + 7
        # Use DP by 1D array to store the number of ways to construct a good string with length i
        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1
        for i in range(min(zero, one), high + 1):
            dp[i] = (dp[i] + dp[i - zero] + dp[i - one]) % MOD
        # Compute the total number of ways to construct a good string with length i from low to high
        ans = 0
        for i in range(low, high + 1):
            ans = (ans + dp[i]) % MOD
        return int(ans)
