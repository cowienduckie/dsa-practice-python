from typing import List


class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * size

    def add(self, idx: int, delta: int) -> None:
        while idx < self.size:
            self.tree[idx] += delta
            idx |= idx + 1

    def sum(self, idx: int) -> None:
        ans = 0
        while idx >= 0:
            ans += self.tree[idx]
            idx = (idx & (idx + 1)) - 1
        return ans


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Use an array to store index map from array 1 to array 2 for same number
        memo = {num: i for i, num in enumerate(nums2)}
        index_map = [memo[num] for num in nums1]

        # Given number X at index i in array 1, and at index j in array 2
        # Because we traverse by indices of array 1, so there are i numbers have index smaller than i in array 1
        # By using Fenwick Tree, quickly find how many numbers have index smaller than X in both array
        bit = FenwickTree(n)
        ans = 0

        for i in range(n):
            # Get j from index map
            j = index_map[i]

            # Find how many numbers have indices smaller than both i and j in 2 arrays
            prefix = bit.sum(j)

            # Add j into BIT
            bit.add(j, 1)

            # Find how many numbers have indices more than both i and j in 2 arrays
            suffix = (n - 1 - j) - (i - prefix)

            # Update the answer
            ans += prefix * suffix

        return ans
