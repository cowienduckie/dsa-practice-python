from math import inf
from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        memo = {}
        ans = inf
        for i, num in enumerate(nums):
            if num in memo:
                ans = min(ans, i - memo[num])
            memo[self._reverse(num)] = i
        return ans if ans != inf else -1

    def _reverse(self, num) -> int:
        return int(str(num)[::-1])
