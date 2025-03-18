from typing import List


class Solution:
    """
    Solution using sliding window
    """

    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Initiate the window and left pointer
        l = window = ans = 0

        # Move right pointer
        for r in range(n):
            # Try to pop elements on left pointer
            # Make sure no set bit of nums[r] is already set in sliding window
            while l < r and window & nums[r]:
                window ^= nums[l]
                l += 1

            # Add the element of right pointer in to window
            window |= nums[r]

            # Update final answer
            ans = max(ans, r - l + 1)
        return ans
