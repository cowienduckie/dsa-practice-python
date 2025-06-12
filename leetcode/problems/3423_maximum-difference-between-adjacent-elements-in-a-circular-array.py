from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_dist = abs(nums[0] - nums[-1])
        for i in range(len(nums) - 1):
            max_dist = max(max_dist, abs(nums[i] - nums[i + 1]))

        return max_dist
