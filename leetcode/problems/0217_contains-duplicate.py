from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set: Set[int] = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False
