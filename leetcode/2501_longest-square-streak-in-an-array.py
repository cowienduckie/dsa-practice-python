from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n = len(nums)
        dp = dict()
        nums.sort()
        for i in range(n - 1, -1, -1):
            if nums[i] in dp:
                continue
            dp[nums[i]] = dp.get(nums[i] * nums[i], 0) + 1

        ans = 1
        for val in dp.values():
            ans = max(ans, val)

        return ans if ans > 1 else -1


class Solution2:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0

        for num in nums_set:
            streak = 0
            while num in nums_set:
                streak += 1
                num *= num
            ans = max(ans, streak)

        return ans if ans > 1 else -1
