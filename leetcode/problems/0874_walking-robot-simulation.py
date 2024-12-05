from typing import List, Dict, Tuple


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Use 2 dict to store obstacles by col and by row
        obs_by_x: Dict[int, set[int]] = dict()
        obs_by_y: Dict[int, set[int]] = dict()

        for [x, y] in obstacles:
            if not x in obs_by_x:
                obs_by_x[x] = set()
            if not y in obs_by_y:
                obs_by_y[y] = set()
            obs_by_x[x].add(y)
            obs_by_y[y].add(x)

        # Loop through commands and maintain max Euclidean distance
        # North = 1, East = 2, South = 3, West = 4
        def change_direction(curr_dir: int, turn_dir: int) -> int:
            if turn_dir == -2:
                curr_dir -= 1
            elif turn_dir == -1:
                curr_dir += 1

            if curr_dir == 0:
                return 4
            elif curr_dir == 5:
                return 1
            return curr_dir

        def move(x: int, y: int, dir: int, step: int) -> Tuple[int, int]:
            if dir == 1:  # Increase Y
                for i in range(1, step + 1):
                    if x in obs_by_x and (y + i) in obs_by_x[x]:
                        return x, y + i - 1
                return x, y + step
            elif dir == 2:  # Increase X
                for i in range(1, step + 1):
                    if y in obs_by_y and (x + i) in obs_by_y[y]:
                        return x + i - 1, y
                return x + step, y
            elif dir == 3:  # Decrease Y
                for i in range(1, step + 1):
                    if x in obs_by_x and (y - i) in obs_by_x[x]:
                        return x, y - i + 1
                return x, y - step
            elif dir == 4:  # Decrease X
                for i in range(1, step + 1):
                    if y in obs_by_y and (x - i) in obs_by_y[y]:
                        return x - i + 1, y
                return x - step, y

        # Start at (0, 0) facing North
        x, y = 0, 0
        dir = 1
        ans = float("-inf")

        for comm in commands:
            if comm < 0:
                dir = change_direction(dir, comm)
            else:
                x, y = move(x, y, dir, comm)
                ans = max(ans, x * x + y * y)

        return ans


commands = [-2, -1, 8, 9, 6]
obstacles = [
    [-1, 3],
    [0, 1],
    [-1, 5],
    [-2, -4],
    [5, 4],
    [-2, -3],
    [5, -1],
    [1, -1],
    [5, 5],
    [5, 2],
]
print(Solution().robotSim(commands, obstacles))
