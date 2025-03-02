from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        # Initialize a fixed array with length of maximum id
        memo = [0] * 1001

        # Add ids and values from array 1
        for i, val in nums1:
            memo[i] += val

        # Add ids and values from array 2
        for i, val in nums2:
            memo[i] += val

        # Ignore all elements with value equal to 0
        return [[i, val] for i, val in enumerate(memo) if val != 0]
