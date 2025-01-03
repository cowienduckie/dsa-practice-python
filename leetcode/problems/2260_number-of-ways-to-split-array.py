from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        # Use an array to store the prefix sum before index i
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        # Use an array to store the suffix sum after index i
        suffix = [0] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]
        # Combine the prefix and suffix sum to find the number of ways to split the array
        ans = 0
        for i in range(n - 1):
            if prefix[i + 1] >= suffix[i]:
                ans += 1
        return ans
