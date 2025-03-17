from collections import defaultdict
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Count occurrences of each number
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1
        # Check if any number has odd occurrence, return False
        for cnt in memo.values():
            if cnt & 1:
                return False
        return True
