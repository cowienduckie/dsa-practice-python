from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = "aeiou"

        # Use prefix sum to store the number of words that start and end with a vowel
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + (
                1 if words[i - 1][0] in vowels and words[i - 1][-1] in vowels else 0
            )

        # Find the number of words that start and end with a vowel in the range of queries
        ans = []
        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])
        return ans
