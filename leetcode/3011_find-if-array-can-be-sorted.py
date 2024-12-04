from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def set_bits(num: int) -> int:
            i, ans = 8, 0
            while (pow_two := 2**i) >= 1:
                if num >= pow_two:
                    ans = ans + 1
                    num = num - pow_two
                i = i - 1
            return ans

        bits = [set_bits(x) for x in nums]

        for i in range(1, len(nums)):
            if bits[i] < bits[i - 1]:
                return False
        return True


class Solution:
    """
    Sorter solution using built-in bit_count() function.
    """

    def canSortArray(self, nums: List[int]) -> bool:
        last_max, curr_max = float("-inf"), nums[0]

        for i in range(1, len(nums)):
            if nums[i].bit_count() == nums[i - 1].bit_count():
                curr_max = max(curr_max, nums[i])
            else:
                (last_max, curr_max) = (curr_max, nums[i])

            if nums[i] < last_max:
                return False

        return True
