from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Use two 2D arrays to store whether a cell can reach the Pacific (top-left) and Atlantic (bottom-right)
        top_left = [[c == 0 or r == 0 for c in range(cols)] for r in range(rows)]
        bot_right = [
            [c == cols - 1 or r == rows - 1 for c in range(cols)] for r in range(rows)
        ]

        # Use DFS to spread if the water can flow from the node to the neighbor
        def dfs(
            row: int,
            col: int,
            visited: List[List[bool]],
        ) -> None:
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and heights[new_row][new_col] >= heights[row][col]
                    and not visited[new_row][new_col]
                ):
                    visited[new_row][new_col] = True
                    dfs(new_row, new_col, visited)

        # We already know that only the edge cells can reach the Pacific and Atlantic initially
        # So, we only need to start from the edge cells
        for row in range(rows):
            dfs(row, 0, top_left)
            dfs(row, cols - 1, bot_right)

        for col in range(cols):
            dfs(0, col, top_left)
            dfs(rows - 1, col, bot_right)

        # Find the cells that can reach both the Pacific and Atlantic
        return [
            [row, col]
            for row in range(rows)
            for col in range(cols)
            if top_left[row][col] and bot_right[row][col]
        ]


heights = [
    [11, 3, 2, 4, 14, 6, 13, 18, 1, 4, 12, 2, 4, 1, 16],
    [5, 11, 18, 0, 15, 14, 6, 17, 2, 17, 19, 15, 12, 3, 14],
    [10, 2, 5, 13, 11, 11, 13, 19, 11, 17, 14, 18, 14, 3, 11],
    [14, 2, 10, 7, 5, 11, 6, 11, 15, 11, 6, 11, 12, 3, 11],
    [13, 1, 16, 15, 8, 2, 16, 10, 9, 9, 10, 14, 7, 15, 13],
    [17, 12, 4, 17, 16, 5, 0, 4, 10, 15, 15, 15, 14, 5, 18],
    [9, 13, 18, 4, 14, 6, 7, 8, 5, 5, 6, 16, 13, 7, 2],
    [19, 9, 16, 19, 16, 6, 1, 11, 7, 2, 12, 10, 9, 18, 19],
    [19, 5, 19, 10, 7, 18, 6, 10, 7, 12, 14, 8, 4, 11, 16],
    [13, 3, 18, 9, 16, 12, 1, 0, 1, 14, 2, 6, 1, 16, 6],
    [14, 1, 12, 16, 7, 15, 9, 19, 14, 4, 16, 6, 11, 15, 7],
    [6, 15, 19, 13, 3, 2, 13, 7, 19, 11, 13, 16, 0, 16, 16],
    [1, 5, 9, 7, 12, 9, 2, 18, 6, 12, 1, 8, 1, 10, 19],
    [10, 11, 10, 11, 3, 5, 12, 0, 0, 8, 15, 7, 5, 13, 19],
    [8, 1, 17, 18, 3, 6, 8, 15, 0, 9, 8, 8, 12, 5, 18],
    [8, 3, 6, 12, 18, 15, 10, 10, 12, 19, 16, 7, 17, 17, 1],
    [12, 13, 6, 4, 12, 18, 18, 9, 4, 9, 13, 11, 5, 3, 14],
    [8, 4, 12, 11, 2, 2, 10, 3, 11, 17, 14, 2, 17, 4, 7],
    [8, 0, 14, 0, 13, 17, 11, 0, 16, 13, 15, 17, 4, 8, 3],
    [18, 15, 8, 11, 18, 3, 10, 18, 3, 3, 15, 9, 11, 15, 15],
]

print(
    Solution().pacificAtlantic(heights)
)  # Answer: [[0,14],[1,14],[2,14],[3,14],[4,13],[4,14],[5,14],[19,0]]
