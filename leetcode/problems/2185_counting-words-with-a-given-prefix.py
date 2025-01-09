from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([1 for word in words if word.startswith(pref)])
