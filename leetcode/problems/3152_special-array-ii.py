from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        # Compute the best starting index of perfect sub-array ending at each position
        prefix = [0] * n
        for i in range(1, n):
            # If number at i has different parity with the i - 1, the perfect sub-array is lengthened
            # Otherwise, start a new one
            if (nums[i] ^ nums[i - 1]) & 1:
                prefix[i] = prefix[i - 1]
            else:
                prefix[i] = i

        # Answer all queries
        # By checking if start index belongs to the perfect sub-array of end index
        return [start >= prefix[end] for start, end in queries]
