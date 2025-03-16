from math import floor, sqrt
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_time = 1
        max_time = max(ranks) * cars * cars

        while min_time <= max_time:
            mid_time = min_time + (max_time - min_time) // 2

            if self._can_fix(ranks, cars, mid_time):
                max_time = mid_time - 1
            else:
                min_time = mid_time + 1

        return min_time

    def _can_fix(self, ranks: List[int], cars: int, time: int) -> bool:
        for r in ranks:
            cars = cars - int(floor(sqrt(time / r)))
            if cars <= 0:
                return True
        return False
