from typing import Tuple


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def check_pair(p1: Tuple[str, str], p2: Tuple[str, str]) -> bool:
            return sorted(p1) == sorted(p2)

        return check_pair((s1[0], s1[2]), (s2[0], s2[2])) and check_pair(
            (s1[1], s1[3]), (s2[1], s2[3])
        )
