from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        ans = []
        n = len(digits)

        def make_combinations(pos: int, s: str) -> None:
            if pos == n:
                nonlocal ans
                ans.append(s)
                return

            for char in phone_map[digits[pos]]:
                make_combinations(pos + 1, s + char)

        if n > 0:
            make_combinations(0, "")
        return ans
