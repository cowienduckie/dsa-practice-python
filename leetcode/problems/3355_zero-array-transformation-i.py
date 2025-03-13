from typing import List


class Solution:
    """
    Solution using line sweep
    """

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)

        # Store a difference array of ranges
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        # Traverse through both original and difference arrays
        # Try to decrease original number, if any number cannot reach at least 0, return False
        sub = 0
        for i in range(n):
            # Update subtrahend
            sub += diff[i]

            # Check if current number can reach 0
            if nums[i] > sub:
                return False

        return True
