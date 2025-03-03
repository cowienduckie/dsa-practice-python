from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []

        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num < pivot:
                less.append(num)
            else:
                equal.append(num)

        return less + equal + greater
