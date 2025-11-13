from collections import defaultdict
from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        # Use dictionary to store frequency of all numbers in nums2
        self.memo = defaultdict(int)
        for num in nums2:
            self.memo[num] += 1

    def add(self, index: int, val: int) -> None:
        self.memo[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.memo[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        cnt = 0
        for num in self.nums1:
            cnt += self.memo[tot - num]
        return cnt
