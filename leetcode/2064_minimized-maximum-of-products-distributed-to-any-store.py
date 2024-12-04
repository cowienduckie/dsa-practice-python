from math import ceil
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Try to distribute the products to the stores with the maximum quantity of each store
        def can_distribute(maximum: int) -> bool:
            total = 0
            for quantity in quantities:
                total += int(ceil(quantity / maximum))
                if total > n:
                    return False
            return total <= n

        # Binary search the minimum maximum quantity
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1

        return left
