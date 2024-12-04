from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)

        # Store the status of whether the substring [0, start) can be broken into words.
        dp = [True] + [False] * n

        for start in range(n):
            # If the substring [0, start) can be broken into words
            # Check if the substring from [start, end) can be broken into words.
            if dp[start]:
                for end in range(start + 1, n + 1):
                    dp[end] = dp[end] or s[start:end] in word_set

        return dp[n]
