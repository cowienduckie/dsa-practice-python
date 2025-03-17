from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        memo = defaultdict(list)

        for i, num in enumerate(nums):
            memo[num].append(i)

        ans = []
        for q in queries:
            indices = memo[nums[q]]

            if len(indices) == 1:
                ans.append(-1)
            else:
                i = bisect_left(indices, q)

                j1 = indices[i - 1]
                j2 = indices[(i + 1) % len(indices)]

                d1 = abs(q - j1)
                d2 = abs(q - j2)

                ans.append(min(d1, d2, n - d1, n - d2))

        return ans
