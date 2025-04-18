from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Use dictionary to store frequency of each number in the window
        freq = defaultdict(int)
        l = ans = pairs = 0

        # Slide the window left to right
        for r in range(len(nums)):
            # Update number of pairs and frequency of number at right
            pairs += freq[nums[r]]
            freq[nums[r]] += 1

            # Try to shrink current window as small as possible
            while pairs >= k:
                # Update number of pairs and frequency of number at left
                freq[nums[l]] -= 1
                pairs -= freq[nums[l]]

                # Update left pointer
                l += 1

            # Update answer
            ans += l
        return ans
