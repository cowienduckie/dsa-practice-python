from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        row_cnt = [0] * rows
        col_cnt = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    row_cnt[r] += 1
                    col_cnt[c] += 1
        
        special = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and row_cnt[r] == 1 and col_cnt[c] == 1:
                    special += 1
        return special