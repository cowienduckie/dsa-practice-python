from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Base case
        n = len(nums)
        if n < 3:
            return []

        # Sort the array ascending
        nums.sort()

        # Pick nums[i] first, then use two pointers to find a pair has sum equal to -nums[i]
        ans = []
        for i in range(n - 2):
            # Skip the checked nums[i] to avoid duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            l = i + 1
            r = n - 1
            while l < r:
                while l < r - 1 and nums[l] + nums[r] != target:
                    # If current sum smaller than target move left pointer to increase
                    # Otherwise, move right pointer to decrease
                    if nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
                # If we find a valid triplet, put them into answer
                if nums[l] + nums[r] == target:
                    ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # Skip the same left pointer's value to avoid duplicate triplets
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                # Skip the same right pointer's value to avoid duplicate triplets
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
        return ans
