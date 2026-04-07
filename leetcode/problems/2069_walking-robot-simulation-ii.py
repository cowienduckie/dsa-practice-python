from typing import List, Tuple


class Direction:
    def __init__(self, name: str, dx: int, dy: int, boundary: Tuple[int, int]):
        self.name = name
        self.dx = dx
        self.dy = dy
        self.boundary = boundary


class Robot:

    def __init__(self, width: int, height: int):
        self.perimeter = ((width - 1) + (height - 1)) * 2
        self.directions = [
            Direction("East", 1, 0, (width - 1, 0)),
            Direction("North", 0, 1, (width - 1, height - 1)),
            Direction("West", -1, 0, (0, height - 1)),
            Direction("South", 0, -1, (0, 0)),
        ]
        self.boundaries = [d.boundary for d in self.directions]
        self.x = 0
        self.y = 0
        self.d = 0
        self.curr_dir = self.directions[0]

    def step(self, step: int) -> None:
        if step >= self.perimeter:
            step = self._move_on_perimeter(step)

        while step:
            step = self._move_on_edge(step)

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.curr_dir.name

    def _move_on_perimeter(self, step: int) -> int:
        leftover = step % self.perimeter

        # If starting points is corner, consider the ending direction if no leftover step
        if (
            (self.x, self.y) in self.boundaries
            and not leftover
            and self._dist_to_boundary()
        ):
            self._rotate(counter_clockwise=False)

        return leftover

    def _move_on_edge(self, max_step: int) -> int:
        max_dist = self._dist_to_boundary()
        if not max_dist:
            self._rotate()

        if max_step < max_dist:
            self.x += max_step * self.curr_dir.dx
            self.y += max_step * self.curr_dir.dy
            return 0
        else:
            self.x += max_dist * self.curr_dir.dx
            self.y += max_dist * self.curr_dir.dy
            return max_step - max_dist

    def _rotate(self, counter_clockwise: bool = True) -> None:
        if counter_clockwise:
            self.d = (self.d + 1) % 4
        else:
            self.d = (self.d + 3) % 4
        self.curr_dir = self.directions[self.d]

    def _dist_to_boundary(self) -> int:
        # Move horizontally
        if self.curr_dir.dy == 0:
            return abs(self.curr_dir.boundary[0] - self.x)
        # Move vertically
        else:
            return abs(self.curr_dir.boundary[1] - self.y)
