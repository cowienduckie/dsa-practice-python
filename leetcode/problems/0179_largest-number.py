from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert original list of integers to list of strings
        # and sort them in descending order
        num_str = list(map(str, nums))
        num_str.sort(
            key=cmp_to_key(lambda a, b: 1 if a + b > b + a else -1), reverse=True
        )

        if num_str[0] == "0":
            return "0"
        else:
            return "".join(num_str)
