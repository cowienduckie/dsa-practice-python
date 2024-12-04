from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_min = n - 1

        for i in range(n - 2, -1, -1):
            if nums[i] + i >= curr_min:
                curr_min = i

        return curr_min == 0
