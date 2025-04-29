from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Find the max number in array
        max_num = max(nums)

        # Use sliding window to keep track number of max_num
        ans = cnt = l = 0
        for r in range(len(nums)):
            # Increase counter if right pointer is max_num
            if nums[r] == max_num:
                cnt += 1
            # Try to shrink the window if the current window have exact k max_num
            if cnt == k:
                # Move left pointer to leftmost max_num
                while nums[l] != max_num:
                    l += 1
                # Remove the leftmost max_num
                cnt -= 1
                l += 1
            # Update the answer by position of left pointer
            ans += l
        return ans
