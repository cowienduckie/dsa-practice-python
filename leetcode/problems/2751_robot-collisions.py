from typing import List, Self


class Robot:
    def __init__(self, id: int, pos: int, hp: int, dir: str):
        self.id = id
        self.pos = pos
        self.hp = hp
        self.dir = dir

    def lose_hp(self) -> None:
        self.hp -= 1

    def die(self) -> None:
        self.hp = 0

    def is_alive(self) -> bool:
        return self.hp > 0

    def fight(self, opp: Self) -> None:
        if self.hp < opp.hp:
            self.die()
            opp.lose_hp()
        elif self.hp > opp.hp:
            self.lose_hp()
            opp.die()
        else:
            self.die()
            opp.die()


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:

        robots = sorted(
            [
                Robot(i, positions[i], healths[i], directions[i])
                for i in range(len(positions))
            ],
            key=lambda r: r.pos,
        )
        stack = []

        for robot in robots:

            while (
                stack and stack[-1].dir == "R" and robot.dir == "L" and robot.is_alive()
            ):
                stack_robot = stack.pop()
                robot.fight(stack_robot)

                if stack_robot.is_alive():
                    stack.append(stack_robot)

            if robot.is_alive():
                stack.append(robot)

        return [robot.hp for robot in sorted(stack, key=lambda r: r.id)]
