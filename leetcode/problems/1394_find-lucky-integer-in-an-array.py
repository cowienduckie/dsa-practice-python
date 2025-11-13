from collections import defaultdict
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        memo = defaultdict(int)

        for num in arr:
            memo[num] += 1

        ans = -1
        for k, v in memo.items():
            if k == v:
                ans = max(ans, k)

        return ans
