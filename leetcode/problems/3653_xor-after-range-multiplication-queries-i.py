from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1_000_000_007
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        ans = 0
        for num in nums:
            ans ^= num
        return ans
