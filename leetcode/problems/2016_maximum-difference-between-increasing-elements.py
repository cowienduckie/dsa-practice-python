from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        diff = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                diff = max(diff, nums[j] - nums[i])

        return diff if diff > 0 else -1
