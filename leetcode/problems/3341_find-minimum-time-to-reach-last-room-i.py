from heapq import heappop, heappush
from typing import List


class Solution:
    def minTimeToReach(self, room_unlocked: List[List[int]]) -> int:
        # Define constants
        NUM_ROWS, NUM_COLS = len(room_unlocked), len(room_unlocked[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Using a min-heap to store the earliest visiting time and coordinates of the rooms
        # Keep track visited rooms to avoid cycles
        visited = [[False] * NUM_COLS for _ in range(NUM_ROWS)]
        heap = [(0, 0, 0)]

        while heap:
            time, row, col = heappop(heap)

            # If we reach the last room, return the time
            if row == NUM_ROWS - 1 and col == NUM_COLS - 1:
                return time

            # If the room is already visited, skip it
            if visited[row][col]:
                continue
            visited[row][col] = True

            for dr, dc in DIRECTIONS:
                nr = row + dr
                nc = col + dc
                # Check if the new coordinates are within bounds and not visited
                if 0 <= nr < NUM_ROWS and 0 <= nc < NUM_COLS and not visited[nr][nc]:
                    # When moving to a new room, we need to wait until the room is unlocked then it take 1 more second to get in
                    heappush(heap, (max(room_unlocked[nr][nc] + 1, time + 1), nr, nc))
        return -1


print(Solution().minTimeToReach([[0, 4], [4, 4]]))
