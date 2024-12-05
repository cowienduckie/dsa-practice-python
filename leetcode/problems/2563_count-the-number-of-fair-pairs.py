from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    """
    Solution using two-pointer and binary search with built-in bisect_left and bisect_right
    """

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n, ans = len(nums), 0
        nums.sort()

        for i in range(n):
            left_pos = bisect_left(nums, lower - nums[i], i + 1)
            right_pos = bisect_right(nums, upper - nums[i], i + 1)
            ans += right_pos - left_pos
        return ans


print(Solution().countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))
