from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans, curr = 1, 0
        for i in range(1, len(nums)):
            # Start a new subarray
            if curr == 0:
                if nums[i] > nums[i - 1]:
                    curr = 2
                elif nums[i] < nums[i - 1]:
                    curr = -2
            # Curr subarray is increasing
            elif curr > 0:
                if nums[i] > nums[i - 1]:
                    curr += 1
                elif nums[i] < nums[i - 1]:
                    curr = -2
                else:
                    curr = 0
            # Curr subarray is decreasing
            elif curr < 0:
                if nums[i] < nums[i - 1]:
                    curr -= 1
                elif nums[i] > nums[i - 1]:
                    curr = 2
                else:
                    curr = 0
            # Update answer
            ans = max(ans, abs(curr))
        return ans
