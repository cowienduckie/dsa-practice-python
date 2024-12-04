from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Bitwise AND of an array always equal or less than the maximum element
        # Find the maximum element in the list
        # Then, find the longest sub-array of that maximum element
        max_num = float("-inf")
        for num in nums:
            max_num = max(max_num, num)

        ans = float("-inf")
        curr_len = 0
        for num in nums:
            if num == max_num:
                curr_len += 1
            elif curr_len > 0:
                ans = max(ans, curr_len)
                curr_len = 0

        return ans if curr_len == 0 else max(ans, curr_len)
