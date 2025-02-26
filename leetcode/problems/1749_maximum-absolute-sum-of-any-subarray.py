from typing import List


class Solution:
    """
    Solution using DP and prefix sum thinking

    Given prefix sum arrays, at every index i, we can compute sums of every subarrays ending at i by:
        subarray_sum = prefix[i] - prefix[j]

    We can easily recognize that optimal values for prefix[j] could be in 2 cases:
        - Maximum positive
        - Minimum negative

    So, we iterate through the original array and keep tracking prefix[i], optimal values of prefix[j]

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Iterate though every index i, update answer by max absolute sum of subarrays ending at i
        ans = curr_sum = max_pos = min_neg = 0

        for num in nums:
            # Update current sum
            curr_sum += num

            # Update maximum positive and minimum negative prefix sum
            max_pos = max(max_pos, curr_sum)
            min_neg = min(min_neg, curr_sum)

            # Update final answer
            ans = max(ans, abs(curr_sum - min_neg), abs(curr_sum - max_pos))

        return ans
