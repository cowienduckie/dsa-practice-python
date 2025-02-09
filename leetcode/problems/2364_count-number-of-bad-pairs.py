from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        # Track frequency of the subtraction of nums[i] with its index
        memo = defaultdict(int)
        for i in range(n):
            memo[nums[i] - i] += 1

        # Compute total of pairs available
        total_pairs = n * (n - 1) // 2

        # Check each subtraction to count number of good pairs
        good_pairs = 0
        for p in memo.values():
            good_pairs += p * (p - 1) // 2

        # The leftovers are bad pairs
        return total_pairs - good_pairs
