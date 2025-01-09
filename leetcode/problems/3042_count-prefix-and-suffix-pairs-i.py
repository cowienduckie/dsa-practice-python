from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n, ans = len(words), 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans

    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        l1, l2 = len(str1), len(str2)
        return l1 <= l2 and str1 == str2[:l1] == str2[l2 - l1 :]


class Solution:
    """
    Pythonic solution
    """

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return len(
            [
                1
                for i in range(len(words))
                for j in range(i + 1, len(words))
                if words[j].startswith(words[i]) and words[j].endswith(words[i])
            ]
        )
