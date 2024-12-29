from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, m, MOD = len(target), len(words[0]), 1e9 + 7
        if m < n:
            return 0

        # Store the characters in words at each index
        freq = [{} for _ in range(m)]
        for k in range(m):
            for word in words:
                freq[k][word[k]] = freq[k].get(word[k], 0) + 1

        # Use bottom-up DP to build up answers
        dp = [[0] * m for _ in range(n)]

        for k in range(m):
            dp[0][k] = freq[k].get(target[0], 0)

        for i in range(1, n):
            for k in range(i, i + m - n + 1):
                if target[i] not in freq[k]:
                    continue
                for x in range(i - 1, k):
                    dp[i][k] += (
                        (freq[k][target[i]] % MOD) * (dp[i - 1][x] % MOD)
                    ) % MOD

        # Compute the answer
        ans = 0
        for k in range(m):
            ans = (ans + dp[n - 1][k]) % MOD

        return int(ans)
