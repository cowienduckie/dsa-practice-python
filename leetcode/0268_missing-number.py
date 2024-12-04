from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for i in range(n):
            ans ^= i ^ nums[i]
        return ans ^ n
