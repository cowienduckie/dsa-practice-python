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
        heap = [(0, 2, 0, 0)]

        while heap:
            time, delta, row, col = heappop(heap)

            # If we reach the last room, return the time
            if row == NUM_ROWS - 1 and col == NUM_COLS - 1:
                return time

            # If the room is already visited, skip it
            if visited[row][col]:
                continue
            visited[row][col] = True

            # Rotate the needed time to move between rooms
            delta = 2 if delta == 1 else 1

            for dr, dc in DIRECTIONS:
                next_row = row + dr
                next_col = col + dc
                # Check if the new coordinates are within bounds and not visited
                if (
                    0 <= next_row < NUM_ROWS
                    and 0 <= next_col < NUM_COLS
                    and not visited[next_row][next_col]
                ):
                    # When moving to a new room, we need to wait until the room is unlocked then it take delta more second to get in
                    heappush(
                        heap,
                        (
                            max(
                                room_unlocked[next_row][next_col] + delta, time + delta
                            ),
                            delta,
                            next_row,
                            next_col,
                        ),
                    )
        return -1
