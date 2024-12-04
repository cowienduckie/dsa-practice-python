from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits_count = [0] * 24  # log2(10^7) = 23.25

        def count_set_bits(num: int) -> None:
            exp = 23
            while (two_pow := 2**exp) >= 1:
                if num >= two_pow:
                    bits_count[exp] += 1
                    num -= two_pow
                exp -= 1

        for num in candidates:
            count_set_bits(num)

        return max(bits_count)
