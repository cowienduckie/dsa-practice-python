from typing import List, Set, Tuple

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]  # N -> E -> S -> W


class Robot:
    def __init__(self, obs: Set[Tuple]):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.max_dist = 0
        self.obs = obs

    def execute_command(self, command: int) -> None:
        if command > 0:
            self._move(command)
        else:
            self._rotate(command == -1)

    def _move(self, step: int) -> None:
        dx, dy = directions[self.dir]

        for _ in range(step):
            next_x = self.x + dx
            next_y = self.y + dy
            if self._is_obstacle(next_x, next_y):
                break
            self.x = next_x
            self.y = next_y

        self._capture_dist()

    def _rotate(self, clockwise: bool) -> None:
        if clockwise:
            self.dir = (self.dir + 1) % 4
        else:
            self.dir = (self.dir + 3) % 4

    def _capture_dist(self) -> None:
        self.max_dist = max(self.max_dist, self.x**2 + self.y**2)

    def _is_obstacle(self, x: int, y: int) -> bool:
        return (x, y) in self.obs


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        robot = Robot(set(map(tuple, obstacles)))
        for command in commands:
            robot.execute_command(command)

        return robot.max_dist
