from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        # Use DFS to check every subset of array
        def dfs(i: int, xor: int) -> None:
            # Base case
            if i == len(nums):
                nonlocal ans
                ans += xor
                return
            # Take or not take i-th number
            dfs(i + 1, xor)
            dfs(i + 1, xor ^ nums[i])

        dfs(0, 0)
        return ans
