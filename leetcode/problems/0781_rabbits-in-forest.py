from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Count the rabbits having same answers and group them
        # Add 1 to their answer as they are counting themself
        memo = defaultdict(int)
        for num in answers:
            memo[num + 1] += 1

        # Consider a group of V rabbits answering K
        # If V <= K, they may have same color and there are (K - V) other rabbits with that color
        # If V > K, we can split them to multiple K-size groups
        ans = 0
        for k, v in memo.items():
            ans += k * int(ceil(v / k))
        return ans
