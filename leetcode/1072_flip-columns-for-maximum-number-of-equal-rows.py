from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        memo = dict()
        for row in matrix:
            # If we treat each row as a bitset, there're only 2 ways to get all-0 and all-1 bitset
            # XOR with its inverted bitset or XOR with itself
            bits = tuple(row)
            inverted = tuple([bit ^ 1 for bit in bits])

            # Collect all bitset could make a row become all-0 or all-1
            # Then return the maximum
            memo[bits] = memo.get(bits, 0) + 1
            memo[inverted] = memo.get(inverted, 0) + 1

        return max(memo.values())
