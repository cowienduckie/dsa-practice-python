from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        memo = dict()
        for num in nums:
            memo[num] = memo.get(num, 0) + 1
            if memo[num] > target:
                return num

        return -1


class Solution:
    """
    Use Boyer-Moore Voting Algorithm to find the majority element.
    """

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
