from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Sort original array ascending
        nums.sort()

        # Fix the first number ans use 2 pointers to iterate through all the possible closest to target
        ans = 1e6
        for i in range(n - 2):
            # Skip the checked first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to traverse the other two numbers
            l, r = i + 1, n - 1
            while l < r:
                # Compute current sum
                curr_sum = nums[i] + nums[l] + nums[r]

                # Try to update current answer
                if abs(curr_sum - target) < abs(ans - target):
                    ans = curr_sum

                # Early return if current sum exactly equal to target
                if curr_sum == target:
                    return target

                # Update the pointers to make current sum likely closer to target
                if curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return ans
