import string
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Store number of each word in a dictionary
        memo = {}
        for word in words:
            memo[word] = memo.get(word, 0) + 1

        # Try to find all word pairs to construct a palindrome
        ans = 0
        for word in memo:
            # If word have 2 same letters, it only can make a pair with itself
            if word[0] == word[1]:
                pairs = memo[word] // 2
                ans += pairs * 4
                memo[word] -= pairs * 2
            # Otherwise, make pair each word with its reversed one
            else:
                rev = word[::-1]
                if rev not in memo:
                    continue
                pairs = min(memo[word], memo[rev])
                ans += pairs * 4
                memo[word] -= pairs
                memo[rev] -= pairs

        # Check the leftovers to find a word with 2 same letters to use as center word
        for c in list(string.ascii_lowercase):
            if memo.get(c + c, 0) > 0:
                return ans + 2
        return ans
