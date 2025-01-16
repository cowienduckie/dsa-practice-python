from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2) & 1:
            for num in nums1:
                ans ^= num
        if len(nums1) & 1:
            for num in nums2:
                ans ^= num
        return ans
