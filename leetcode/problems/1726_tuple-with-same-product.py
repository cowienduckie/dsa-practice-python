from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # Count number of pair with same product
        freq = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                freq[nums[i] * nums[j]] += 1
        # For each valid 2 pairs, we can construct 8 different permutations
        return sum([8 * (p * (p - 1) // 2) for p in freq.values() if p > 1])
