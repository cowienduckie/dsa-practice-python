from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Use Sieve of Eratosthenes to find all primes number under right bound
        is_prime = [False, False] + [True] * (right - 1)
        num = 2
        while num * num <= right:
            # If num is prime, mark all multiples of num as not prime
            if is_prime[num]:
                for not_prime in range(num * num, right + 1, num):
                    is_prime[not_prime] = False
            num += 1

        # Traverse from left to right to find the smallest pair
        ans = [float("-inf"), float("inf")]
        stack = []

        for num in range(left, right + 1):
            # Skip if num is not prime, skip
            if not is_prime[num]:
                continue

            # Check the prime with top of the stack
            if stack and num - stack[-1] < ans[1] - ans[0]:
                ans[0], ans[1] = stack[-1], num

            # Append prime to stack
            stack.append(num)

        # Return the answer if there are more than 1 prime number
        return ans if len(stack) > 1 else [-1, -1]
