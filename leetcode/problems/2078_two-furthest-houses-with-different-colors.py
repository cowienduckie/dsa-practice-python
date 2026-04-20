from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i in range(n):
            j = n - 1 - i
            if colors[i] != colors[n - 1] or colors[j] != colors[0]:
                ans = max(ans, j)
                break
        return ans
