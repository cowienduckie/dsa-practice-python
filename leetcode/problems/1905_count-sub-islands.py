from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        total_rows = len(grid1)
        total_cols = len(grid1[0])

        # Find all island in grid 1
        island1 = [[0] * total_cols for i in range(total_rows)]
        total_island1 = 0

        for row in range(total_rows):
            for col in range(total_cols):
                if grid1[row][col] == 0 or island1[row][col] > 0:
                    continue
                else:
                    total_island1 = total_island1 + 1
                    self.dfs(
                        grid1, island1, total_island1, row, col, total_rows, total_cols
                    )

        # Find all island in grid 2
        island2 = [[0] * total_cols for i in range(total_rows)]
        total_island2 = 0

        for row in range(total_rows):
            for col in range(total_cols):
                if grid2[row][col] == 0 or island2[row][col] > 0:
                    continue
                else:
                    total_island2 = total_island2 + 1
                    self.dfs(
                        grid2, island2, total_island2, row, col, total_rows, total_cols
                    )

        # Count sub-islands
        sub_islands: dict[int, int] = {}

        for row in range(total_rows):
            for col in range(total_cols):
                # If cell is water in grid 2, skip
                if island2[row][col] == 0:
                    continue

                # If cell is water in grid 1, mark this island cannot be a sub-island
                if island1[row][col] == 0:
                    sub_islands[island2[row][col]] = 0
                    continue

                # If cell is land in both grid 1 and grid 2 but not tracked before, mark this cell belongs to a sub-island
                # Otherwise, check if this cell belongs to the same sub-island with before cells
                if sub_islands.get(island2[row][col]) is None:
                    sub_islands[island2[row][col]] = island1[row][col]
                    continue
                else:
                    if sub_islands[island2[row][col]] != island1[row][col]:
                        sub_islands[island2[row][col]] = 0
                        continue

        return sum([1 for island in sub_islands.values() if island > 0])

    def dfs(
        self,
        grid: List[List[int]],
        island: List[List[int]],
        curr_island: int,
        row: int,
        col: int,
        total_rows: int,
        total_cols: int,
    ) -> None:
        # Check if cell [row, col] is water or belongs to another island, return
        # Otherwise, mark this cell belongs to curr_island
        if (
            row < 0
            or row >= total_rows
            or col < 0
            or col >= total_cols
            or grid[row][col] == 0
            or island[row][col] > 0
        ):
            return
        else:
            island[row][col] = curr_island

            self.dfs(grid, island, curr_island, row + 1, col, total_rows, total_cols)
            self.dfs(grid, island, curr_island, row - 1, col, total_rows, total_cols)
            self.dfs(grid, island, curr_island, row, col + 1, total_rows, total_cols)
            self.dfs(grid, island, curr_island, row, col - 1, total_rows, total_cols)
