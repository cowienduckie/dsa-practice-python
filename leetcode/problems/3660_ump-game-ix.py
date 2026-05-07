from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Build max prefix array of each num
        prefix = list(nums)
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], prefix[i])
        # Build min suffix array of each num
        suffix = list(nums)
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], suffix[i])
        # Build answer array
        ans = list(prefix)
        for i in range(n - 2, -1, -1):
            # At index i, if prefix part (inclusive) has no number higher than the suffix part (exclusive)
            # So we only can make jump from i to the max number of prefix part only
            if prefix[i] <= suffix[i + 1]:
                ans[i] = prefix[i]
            # Otherwise, there is at least 1 way to jump from i to i + 1, so they have the same final answer
            else:
                ans[i] = ans[i + 1]
        return ans
