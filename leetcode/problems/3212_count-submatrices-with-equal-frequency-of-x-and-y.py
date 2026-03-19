from typing import List, Self


class Frequency:
    def __init__(self, value: str):
        self.x = 1 if value == "X" else 0
        self.y = 1 if value == "Y" else 0

    def add(self, freq: Self) -> None:
        self.x += freq.x
        self.y += freq.y

    def subtract(self, freq: Self) -> None:
        self.x -= freq.x
        self.y -= freq.y

    def is_valid(self) -> bool:
        return self.x and self.x == self.y


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Store prefix x-y frequency of each submatrix starting at (0, 0) and ending at (r, c)
        freq = [[Frequency(grid[r][c]) for c in range(cols)] for r in range(rows)]

        count = 0
        for r in range(rows):
            for c in range(cols):
                curr_freq = freq[r][c]
                # Update prefix frequency matrix by top, left, and top-left cells
                if r > 0:
                    curr_freq.add(freq[r - 1][c])
                if c > 0:
                    curr_freq.add(freq[r][c - 1])
                if r > 0 and c > 0:
                    curr_freq.subtract(freq[r - 1][c - 1])
                # Increase total count if frequency of current submatrix is valid
                count += 1 if curr_freq.is_valid() else 0
        return count
