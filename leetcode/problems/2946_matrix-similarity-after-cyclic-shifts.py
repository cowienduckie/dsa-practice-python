from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows, cols = len(mat), len(mat[0])
        k %= cols
        # Early return if k make full shifting cycles
        if k == 0:
            return True
        # Otherwise, check every single row
        for r in range(rows):
            for c1 in range(cols):
                c2 = (c1 + k) % cols if r & 1 else c1 - k
                if mat[r][c1] != mat[r][c2]:
                    return False
        return True
