from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        # Use an array to store the changes at 2 boundaries of an query
        memo = [0] * (n + 1)
        for l, r in queries:
            memo[l] -= 1
            memo[r + 1] += 1
        
        # Move from left to right and track the total diff at each index
        diff = 0
        for i in range(n):
            diff += memo[i]
            # If the diff is not enough to make number i-th reach 0, early return False
            if nums[i] + diff > 0:
                return False
        return True