import bisect
from typing import List, Optional


class Solution:
    def __init__(self):
        self.primes = [num for num in range(2, 1000) if self._is_prime(num)]

    def _is_prime(self, num: int) -> bool:
        if num == 1:
            return False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True

    def _max_valid_prime(self, upper_bound: int) -> Optional[int]:
        max_prime = None
        for p in self.primes:
            if p < upper_bound:
                max_prime = p
            else:
                break
        return max_prime

    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.append(0)

        for i in range(n):
            if p := self._max_valid_prime(nums[i] - nums[i - 1]):
                nums[i] -= p
            elif nums[i] <= nums[i - 1]:
                return False

        return True


class Solution:
    """
    Optimized version by
        - Using bisect to find the maximum prime number that is less than the upper bound.
        - Using a sieve of Eratosthenes to generate prime numbers up to the maximum number in the input.
    """

    def __init__(self):
        self.primes = []

    def _generate_primes(self, limit: int) -> List[int]:
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for start in range(2, int(limit**0.5) + 1):
            if sieve[start]:
                for multiple in range(start * start, limit + 1, start):
                    sieve[multiple] = False
        return [num for num in range(limit + 1) if sieve[num]]

    def _max_valid_prime(self, upper_bound: int) -> Optional[int]:
        idx = bisect.bisect_left(self.primes, upper_bound)
        return self.primes[idx - 1] if idx > 0 else None

    def primeSubOperation(self, nums: List[int]) -> bool:
        max_num = max(nums)
        self.primes = self._generate_primes(max_num)

        n = len(nums)
        nums.append(0)

        for i in range(n):
            if p := self._max_valid_prime(nums[i] - nums[i - 1]):
                nums[i] -= p
            elif nums[i] <= nums[i - 1]:
                return False

        return True
