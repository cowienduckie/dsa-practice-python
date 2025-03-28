from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Solution using brute force DFS to find answer for each query separately.
    """

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        # DFS to count number of cells with value strictly less than q
        def dfs(r: int, c: int, q: int, visited: List[List[bool]]) -> int:
            # Base case: out of bounds or already visited
            if (
                not (0 <= r < rows)
                or not (0 <= c < cols)
                or grid[r][c] >= q
                or visited[r][c]
            ):
                return 0

            # Count this cell and mark it as visited
            points = 1
            visited[r][c] = True

            # Explore all four directions
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                points += dfs(r + dr, c + dc, q, visited)

            return points

        # Iterate through each query and perform DFS
        return [dfs(0, 0, q, [[False] * cols for _ in range(rows)]) for q in queries]


class Solution:
    """
    Solution using BFS and priority queue to pre-compute the maximum points for each possible query.
    """

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        # Helper to check if a cell is valid
        def is_valid_cell(row: int, col: int) -> bool:
            return 0 <= row < rows and 0 <= col < cols

        # Use a min-heap to explore the grid
        # Also keep track of visited cells and the prefix sum of points
        min_heap = [(grid[0][0] + 1, 0, 0)]
        visited = [[False] * cols for _ in range(rows)]
        prefix = [0] * 1_000_002

        while min_heap:
            q, r, c = heappop(min_heap)

            # If we have already visited this cell, skip it
            if visited[r][c]:
                continue

            # Mark the cell as visited and update the prefix sum
            visited[r][c] = True
            prefix[q] += 1

            # Explore all four directions
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if not is_valid_cell(nr, nc):
                    continue
                heappush(min_heap, (max(q, grid[nr][nc] + 1), nr, nc))

        # Compute the prefix sum
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        # Answer the queries using the prefix sum
        return [prefix[q] for q in queries]


class Solution:
    """
    Optimized solution using BFS and priority queue to pre-compute the maximum points for each possible query.
    """

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        min_heap = [(grid[0][0], 0, 0)]  # Use a min-heap to explore the grid
        grid[0][0] = 0  # Mark the cell as visited by setting it to 0
        memo = {}  # Dictionary to store the number of points for each query
        cnt = 0  # Count of points less than the current query

        for q in sorted(queries):
            # If the query is already in the memo, skip it
            if q in memo:
                continue

            # Process the grid until we find all points less than the current query
            while min_heap and min_heap[0][0] < q:
                _, r, c = heappop(min_heap)
                cnt += 1
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    # Check if the new cell is valid and not visited
                    if self._is_valid_cell(nr, nc, grid):
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        grid[nr][nc] = 0

            # If the query is not in the memo, add it
            memo[q] = cnt

        # Form the result list using the memo dictionary but keep the order of queries
        return [memo[q] for q in queries]

    def _is_valid_cell(self, r: int, c: int, grid: List[List[int]]) -> bool:
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]
