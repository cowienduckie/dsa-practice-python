from typing import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_indices_1 = Counter(s1[::2])
        odd_indices_1 = Counter(s1[1::2])
        even_indices_2 = Counter(s2[::2])
        odd_indices_2 = Counter(s2[1::2])

        return even_indices_1 == even_indices_2 and odd_indices_1 == odd_indices_2
