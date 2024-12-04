from typing import List


class Solution(object):
    def nthUglyNumber(self, n: int) -> int:
        primes: List[int] = [2, 3, 5]
        next_ugly: List[int] = [2, 3, 5]
        increase: List[int] = [1, 1, 1]
        arr: List[int] = [1]

        for _ in range(1, n):
            smallest = min(next_ugly)
            arr.append(smallest)

            for i in range(3):
                if next_ugly[i] == smallest:
                    increase[i] += 1
                    next_ugly[i] = primes[i] * arr[increase[i] - 1]

        return arr[-1]
