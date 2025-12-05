class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return 0 if sum(nums) & 1 else len(nums) - 1
