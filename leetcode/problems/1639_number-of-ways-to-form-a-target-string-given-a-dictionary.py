from typing import List


class Solution:
    """
    Solution using bottom-up DP to build up the answer
    The 2D array is used to store the number of ways to form character at index i
    by using only characters from words with index equal or less than j
    """

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
        # We know that in order to form target[i], we can only use characters at index k >= i and k <= i + diff of m and n
        dp = [[0] * m for _ in range(n)]

        # Pre-fill for the first character in target
        for k in range(m):
            dp[0][k] = freq[k].get(target[0], 0)

        for i in range(1, n):
            for k in range(i, i + m - n + 1):
                # Check if the target[i] is can be formed by any character at index k
                if target[i] not in freq[k]:
                    continue
                # Check if the previous character can be formed by any character at index x < k
                for x in range(i - 1, k):
                    dp[i][k] += (
                        (freq[k][target[i]] % MOD) * (dp[i - 1][x] % MOD)
                    ) % MOD

        # Compute the answer
        ans = 0
        for k in range(m):
            ans = (ans + dp[n - 1][k]) % MOD

        return int(ans)
