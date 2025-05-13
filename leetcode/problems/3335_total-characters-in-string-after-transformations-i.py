class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 1_000_000_007

        # Use 2D-array to store length of character i after k transformations
        memo = [[0] * (t + 1) for _ in range(26)]
        for i in range(26):
            for k in range(26 - i):
                memo[i][k] = 1

        # Recursively compute dp[i][k]
        def compute(i: int, k: int) -> int:
            if memo[i][k] == 0:
                # After (26 - i) transformations, character i will become "ab"
                memo[i][k] = (
                    compute(0, k - (26 - i)) % MOD + compute(1, k - (26 - i)) % MOD
                ) % MOD
            return memo[i][k]

        # Break input string into characters
        ans = 0
        for c in s:
            ans = (ans % MOD + compute(ord(c) - ord("a"), t) % MOD) % MOD
        return ans
