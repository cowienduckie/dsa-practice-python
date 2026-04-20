from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i1 = i2 = ans = 0
        while i1 < n1 and i2 < n2:
            # Move i2 pointer
            while i2 < n2 and nums1[i1] <= nums2[i2]:
                i2 += 1
            ans = max(ans, i2 - i1 - 1)
            # Move i pointer
            while i1 < n1 and i2 < n2 and nums1[i1] > nums2[i2]:
                i1 += 1
        return ans
