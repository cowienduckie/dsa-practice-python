from typing import List


class Trie:
    def __init__(self, words: List[str] = None):
        self.root = {}
        self.end_char = "#"
        if words:
            for word in words:
                self.add(word)

    def add(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_char] = None

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_char in node


class Solution:
    """
    Solution based on Trie data structure for learning purposes
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        trie = Trie(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and trie.search(s[start:end]):
                    dp[end] = True
                    break

        return dp[n]


class Solution:
    """
    Optimized solution using Set instead of Trie
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and s[start:end] in word_set:
                    dp[end] = True
                    break
        return dp[n]
