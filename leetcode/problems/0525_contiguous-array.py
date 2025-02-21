from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # Compute prefix diff between 0 and 1, store all indices of a same diff
        prefix = [0] * n
        memo = defaultdict(list)

        # Add -1 as the first position of 0-diff for edge case that max subarray start with index 0
        memo[0].append(-1)

        # Iterate through original array to update prefix and memo
        for i in range(n):
            prefix[i] = prefix[i - 1] + (1 if nums[i] else -1)
            memo[prefix[i]].append(i)

        # For each diff, we only need to check the pair with the greatest distance
        ans = 0
        for indices in memo.values():
            # Skip the diffs exist only once
            if len(indices) == 1:
                continue
            # Update the answer
            ans = max(ans, indices[-1] - indices[0])

        return ans
