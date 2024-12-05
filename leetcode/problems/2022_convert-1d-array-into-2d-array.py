from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Loop through the original array
        # Cut off each row at the counter divisible by n
        mat: List[List[int]] = list()
        row: List[int] = list()

        for i in range(1, len(original) + 1):
            row.append(original[i - 1])
            if i % n == 0:
                mat.append(row)
                row = list()

        if len(mat) != m or len(row) != 0:
            return []
        else:
            return mat


print(Solution().construct2DArray([5, 3, 8, 9, 7, 9, 1, 2, 2, 3, 9], 1, 6))
