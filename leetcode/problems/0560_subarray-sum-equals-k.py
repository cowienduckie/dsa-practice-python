from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    """
    Solution using prefix sum and dictionary
    Given a pair of index (i, j) with i < j and prefix[j] - prefix[i] = k, we can construct a subarray having sum of k
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Compute prefix sum of each index and store the indices of each specific sum
        prefix = [0] * n
        memo = defaultdict(list)

        for i in range(n):
            prefix[i] = prefix[i - 1] + nums[i]
            memo[prefix[i]].append(i)

        # Iterate through dictionary and count the pairs of indices could construct valid subarray
        ans = 0
        for s, idx1 in memo.items():
            # Skip sum s if there is not any sum s + k
            if s + k not in memo:
                continue

            # With each index i in idx1, find how many index j in idx2 that j > i
            idx2 = memo[s + k]
            for i in idx1:
                ans += len(idx2) - bisect_right(idx2, i)

        # With the prefix sum exactly equal to k, we can construct subarray with the whole left part of array
        if k in memo:
            ans += len(memo[k])

        return ans
