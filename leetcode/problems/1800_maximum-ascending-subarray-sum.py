from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = curr = nums[0]
        for i in range(1, len(nums)):
            # If current ASC subarray is broken, reset the current sum
            if nums[i] <= nums[i - 1]:
                ans = max(ans, curr)
                curr = 0
            curr += nums[i]
        return max(ans, curr)
