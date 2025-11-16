class Solution:
    def numSub(self, s: str) -> int:
        MOD = 1_000_000_007
        n = ans = 0
        for c in s + "0":
            if c == "0":
                ans = (ans + ((n + 1) * n // 2) % MOD) % MOD
                n = 0
            else:
                n += 1
        return ans