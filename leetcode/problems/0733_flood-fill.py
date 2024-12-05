from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if (origin := image[sr][sc]) == color:
            return image
        rows = len(image)
        cols = len(image[0])

        def dfs(row: int, col: int) -> None:
            if 0 <= row < rows and 0 <= col < cols and image[row][col] == origin:
                image[row][col] = color

                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        dfs(sr, sc)
        return image
