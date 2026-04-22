from typing import Dict, List


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]

    def diff(
        self, word: str, i: int, curr_dict: Dict[str, Dict], curr_diff: int
    ) -> int:
        # Base cases
        if i == len(word):
            return curr_diff

        if curr_diff == 2 and word[i] not in curr_dict:
            return 3

        # Try to traverse through the trie to calculate minimum diff
        min_diff = 3
        for char, next_dict in curr_dict.items():
            min_diff = min(
                min_diff,
                self.diff(
                    word, i + 1, next_dict, curr_diff + (0 if char == word[i] else 1)
                ),
            )
        return min_diff


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # Build a trie with the dictionary and calculate the diff for each query
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        return [word for word in queries if trie.diff(word, 0, trie.root, 0) <= 2]
