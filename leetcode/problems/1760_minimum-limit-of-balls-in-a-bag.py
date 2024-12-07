from math import ceil
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], max_ops: int) -> int:
        # Use binary search to find the optimal penalty
        low, high = 1, max(nums)

        while low < high:
            penalty = low + (high - low) // 2

            # Find needed number of operations for this penalty
            ops = 0
            for num in nums:
                ops += ceil(num / penalty) - 1

            # Check if the number of operations is exceeded or not
            if ops > max_ops:
                low = penalty + 1
            else:
                high = penalty

        return high
