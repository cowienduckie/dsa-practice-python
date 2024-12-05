from typing import List


class Solution:
    """
    Greedy solution:
        We can always make the matrix positive if the number of negative numbers is even.
        If the number of negative numbers is odd, we can make the matrix positive by flipping the smallest absolute value.

        Example: Assume X and Y are negatives.
            A X  -> A -X -> A  -X
            Y B     Y -B    -Y  B

        Example: Assume X, Y and Z are negatives and |X| < |Y| < |Z|
            A Y -> A -Y -> A  -Y
            Z X    Z -X    -Z  X
    """

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negatives = 0
        sum_abs = 0
        min_abs = float("inf")

        for row in matrix:
            for cell in row:
                sum_abs += abs(cell)
                min_abs = min(min_abs, abs(cell))
                if cell < 0:
                    negatives += 1

        return sum_abs - 2 * min_abs if negatives & 1 else sum_abs
