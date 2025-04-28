from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Use sliding window to count for every valid subarrays
        # For each window, we maintain its sum and length to calculate the score
        ans = window_sum = window_len = l = 0
        for r in range(len(nums)):
            # Add number at right pointer to window, and update sum and length
            window_sum += nums[r]
            window_len += 1

            # Try to shrink the window until score strictly less than k
            while window_sum * window_len >= k:
                window_sum -= nums[l]
                window_len -= 1
                l += 1

            # Update answer with the number of valid subarrays ending at right pointer
            ans += window_len
        return ans
