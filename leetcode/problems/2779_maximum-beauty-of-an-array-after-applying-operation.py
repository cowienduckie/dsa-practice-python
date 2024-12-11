from bisect import bisect_right
from typing import List


class Solution:
    """
    Solution using sorting and binary search.

    We could see that the maximum subsequence of original array must be subarray of the sorted one.
    So, at each index i, the upper bound of the maximum subsequence is the index j where nums[j] - k = nums[i] + k.
    We could use binary search to find the index j for each index i. If j is not out of bound, update the answer.
    """

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Sort the array ascending
        nums.sort()

        # Use binary search to find index j for nums[i] + 2 * k
        # The maximum beauty subsequence starting from i is from i to j
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, bisect_right(nums, nums[i] + 2 * k) - i)

        return ans
