from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        memo = dict()
        curr_sum, max_sum = 0, 0

        for i in range(len(nums)):
            # Add new number to the window
            memo[nums[i]] = memo.get(nums[i], 0) + 1
            curr_sum += nums[i]

            # Remove the leftmost number from the window if the window size is greater than k
            if i > k - 1:
                if memo[nums[i - k]] == 1:
                    memo.pop(nums[i - k])
                else:
                    memo[nums[i - k]] -= 1
                curr_sum -= nums[i - k]

            # Update the maximum sum if the distinct window size is k
            if len(memo) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum
