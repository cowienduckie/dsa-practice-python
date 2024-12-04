from typing import Dict, Optional


class Trie:
    def __init__(self):
        self.root = dict()
        self.end_char = "."

    def insert(self, word: str) -> None:
        # Traverse the trie to insert characters of the word
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = dict()
            curr = curr[char]
        # Mark the end of the word
        curr[self.end_char] = None

    def search(self, word: str) -> bool:
        # Traverse the trie and check if any inserted word ends with the last character
        return (
            last_char := self._trie_traverse(word)
        ) is not None and self.end_char in last_char

    def startsWith(self, prefix: str) -> bool:
        # Different from search, we only need to check if the prefix exists in the trie
        return self._trie_traverse(prefix) is not None

    def _trie_traverse(self, prefix: str) -> Optional[Dict]:
        # Traverse the trie to find the last character
        curr = self.root
        for char in prefix:
            if char not in curr:
                return None
            curr = curr[char]
        return curr
