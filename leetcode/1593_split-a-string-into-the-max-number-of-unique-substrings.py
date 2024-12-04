from typing import Set


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n, ans = len(s), float("-inf")

        # Recursively split the string into unique substrings, for each position, we have two choices:
        # 1. Continue the current substring
        # 2. If the current substring is not in the set, add it to the set and start a new substring
        def slit_string(pos: int, sub_str: str, str_set: Set[str]) -> None:
            if pos == n:
                nonlocal ans
                ans = max(
                    ans, len(str_set)
                )  # The leftovers could be concatenated to last substring, and make no difference to set length
                return

            sub_str += s[pos]
            slit_string(pos + 1, sub_str, str_set)
            if not sub_str in str_set:
                str_set.add(sub_str)
                slit_string(pos + 1, "", str_set)
                str_set.remove(sub_str)

        slit_string(0, "", set())
        return ans
