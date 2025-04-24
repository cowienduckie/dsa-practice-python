from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Pre-count distinct numbers
        total_distinct = len(set(nums))

        # Use sliding window to find and count valid subarray ending at right pointer
        window = defaultdict(int)
        l = ans = 0
        for r in range(len(nums)):
            # Add number at right pointer to window
            window[nums[r]] += 1

            # Try to minimize the size of window
            while len(window) == total_distinct:
                window[nums[l]] -= 1
                # Remove number at left pointer from window if it reaches 0
                if window[nums[l]] == 0:
                    window.pop(nums[l])
                l = l + 1

            # Update answer
            ans += l
        return ans
