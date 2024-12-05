from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Use matrix to store minimum distance from (0, 0) to (r, c)
        min_dist = [[float("inf")] * cols for _ in range(rows)]
        min_dist[0][0] = 0

        # Dijkstra's algorithm using BFS and priority queue
        pq = [(0, 0, 0)]  # (distance, row, col)
        visited = set()
        while pq:
            dist, row, col = heappop(pq)

            # Check if cell has been visited yet
            if (row, col) in visited:
                continue
            visited.add((row, col))

            # Update minimum distance to neighbors
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                # Check if neighbor is out of bound
                nrow, ncol = row + dr, col + dc
                if 0 > nrow or nrow >= rows or 0 > ncol or ncol >= cols:
                    continue

                # Update minimum distance if possible
                ndist = dist + grid[nrow][ncol]

                if ndist < min_dist[nrow][ncol]:
                    min_dist[nrow][ncol] = ndist
                    heappush(pq, (ndist, nrow, ncol))

        return min_dist[rows - 1][cols - 1]
