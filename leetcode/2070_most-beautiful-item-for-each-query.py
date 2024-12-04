from bisect import bisect_right
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort by price ASC then find the maximum beauty for each distinct price
        items.sort(key=lambda x: x[0])
        dp = dict()
        curr_max = float("-inf")

        for p, b in items:
            curr_max = max(curr_max, b)
            dp[p] = curr_max

        # Use binary search from bisect module for faster lookups
        keys = list(dp.keys())

        def find_max_beauty(target: int) -> int:
            if (idx := bisect_right(keys, target) - 1) >= 0:
                return dp[keys[idx]]
            else:
                return 0

        return [find_max_beauty(q) for q in queries]


print(
    Solution().maximumBeauty(
        [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]
    )
)  # [2,4,5,5,6,6]
