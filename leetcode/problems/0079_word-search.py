from typing import List


class Solution:
    """
    Solution using DFS with backtracking to find the word in the board for each cell as a starting point.
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r: int, c: int, k: int) -> bool:
            # If the word is found, return True to escape the recursion
            if k == len(word):
                return True

            # Check if the current cell is out of bounds or visited or not matching the word
            if (
                r < 0
                or r == rows
                or c < 0
                or c == cols
                or visited[r][c]
                or board[r][c] != word[k]
            ):
                return False

            # Mark the cell as visited and explore the neighbors
            visited[r][c] = True
            if (
                dfs(r + 1, c, k + 1)
                or dfs(r - 1, c, k + 1)
                or dfs(r, c + 1, k + 1)
                or dfs(r, c - 1, k + 1)
            ):
                return True

            visited[r][c] = False
            return False

        # Iterate over each cell as starting point to find the word
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
