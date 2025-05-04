from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Use a dictionary to store number of each domino, the key is (a, b) where a <= b
        memo = defaultdict(int)
        for a, b in dominoes:
            if a < b:
                memo[(a, b)] += 1
            else:
                memo[(b, a)] += 1

        # Compute number of pairs from each domino value
        ans = 0
        for cnt in memo.values():
            ans += cnt * (cnt - 1) // 2
        return ans
