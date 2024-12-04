from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            # List does not have enough items to make any triplet
            return []

        # Sort the list and iterate through array to pick the first number in triplet
        # Use 2-pointers method to find the 2 left numbers by checking their sum
        ans = list()
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # Ignore same first number to avoid duplication
                continue
            l = i + 1
            r = n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    # Add result into answers list
                    ans.append(list([nums[i], nums[l], nums[r]]))

                    # Then move both pointers to ignore same triplets to avoid duplication
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
                elif curr_sum < 0:
                    # Move left pointer to increase sum
                    l = l + 1
                else:
                    # Move right pointer to decrease sum
                    r = r - 1
        return ans
