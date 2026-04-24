from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [0] * n
        memo = {}
        for i in range(n):
            if nums[i] in memo:
                j = memo[nums[i]][-1]
                prefix[i] = prefix[j] + (i - j) * len(memo[nums[i]])
                memo[nums[i]].append(i)
            else:
                memo[nums[i]] = [i]

        suffix = [0] * n
        memo = {}
        for i in range(n - 1, -1, -1):
            if nums[i] in memo:
                j = memo[nums[i]][-1]
                suffix[i] = suffix[j] + (j - i) * len(memo[nums[i]])
                memo[nums[i]].append(i)
            else:
                memo[nums[i]] = [i]

        return [p + s for p, s in zip(prefix, suffix)]
