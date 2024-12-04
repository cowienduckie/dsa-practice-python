from collections import deque
from typing import List, Tuple


class Solution:
    """
    Breadth-first search (BFS) Solution:
        We have 6 cells with 6 numbers so that the total number of configurations is 6! = 720.
        It is feasible to use BFS to scan all possible configurations.
    """

    def __init__(self):
        self.end = ((1, 2, 3), (4, 5, 0))
        self.visited = set()
        self.move_dict = {
            (0, 0): [(0, 1), (1, 0)],
            (0, 1): [(0, 0), (0, 2), (1, 1)],
            (0, 2): [(0, 1), (1, 2)],
            (1, 0): [(0, 0), (1, 1)],
            (1, 1): [(1, 0), (1, 2), (0, 1)],
            (1, 2): [(1, 1), (0, 2)],
        }

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Initialize the BFS queue
        start = tuple([tuple(row) for row in board])
        queue = deque([(start, 0)])
        while queue:
            # Return immediately when matching the end configuration
            curr, step = queue.popleft()
            if curr == self.end:
                return step

            # No need to check the visited configuration
            if curr in self.visited:
                continue
            self.visited.add(curr)

            # Add next configurations
            for next_conf in self.nextConfigurations(curr):
                queue.append((next_conf, step + 1))

        return -1

    def nextConfigurations(
        self,
        curr: Tuple[Tuple[int, int, int], Tuple[int, int, int]],
    ) -> List[Tuple[Tuple[int, int, int], Tuple[int, int, int]]]:
        # Convert the configuration to a list of lists
        conf = [list(row) for row in curr]

        # Find the cell containing 0
        row0, col0 = next((i, j) for i in range(2) for j in range(3) if conf[i][j] == 0)

        # Return the next moves of 0-cell
        moves = []
        for dr, dc in self.move_dict[(row0, col0)]:
            new_conf = [row[:] for row in conf]

            new_conf[row0][col0], new_conf[dr][dc] = (
                new_conf[dr][dc],
                new_conf[row0][col0],
            )

            new_conf = tuple(tuple(row) for row in new_conf)
            if new_conf not in self.visited:
                moves.append(new_conf)

        return moves
