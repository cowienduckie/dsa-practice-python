from collections import defaultdict
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        memo = defaultdict(list)
        ans = float("inf")
        for i, num in enumerate(nums):
            if len(memo[num]) > 1:
                ans = min(ans, i - memo[num][-2])
            memo[num].append(i)
        return ans * 2 if ans != float("inf") else -1
