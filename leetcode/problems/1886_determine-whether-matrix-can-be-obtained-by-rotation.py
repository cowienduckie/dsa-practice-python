from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        last = n - 1
        same = rot90 = rot180 = rot270 = True

        for r in range(n):
            for c in range(n):
                value = mat[r][c]
                if same and value != target[r][c]:
                    same = False
                if rot90 and value != target[c][last - r]:
                    rot90 = False
                if rot180 and value != target[last - r][last - c]:
                    rot180 = False
                if rot270 and value != target[last - c][r]:
                    rot270 = False
                if not (same or rot90 or rot180 or rot270):
                    return False

        return same or rot90 or rot180 or rot270
