from typing import List, Set


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_chars = set(allowed)

        def is_consistent(chars: Set[str]) -> bool:
            for char in chars:
                if char not in allowed_chars:
                    return False
            return True

        ans = 0
        for word in words:
            if is_consistent(set(word)):
                ans += 1

        return ans
