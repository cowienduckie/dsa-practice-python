from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        # Check if each tile with index i different from index (i - 1)
        prefix = [1 if colors[i] != colors[i - 1] else 0 for i in range(n)]

        # Pre-compute the total differences in a window with size k
        diff = 0
        for i in range(k - 1):
            diff += prefix[i]

        # Use sliding window to check every k-size windows
        ans = 0
        for i in range(n):
            # Update the differences in current window
            diff -= prefix[i]
            diff += prefix[(i + k - 1) % n]

            # In a k-size window, if there are k - 1 differences, except the first tile
            # This could be an alternating window
            if diff == k - 1:
                ans += 1

        return ans
